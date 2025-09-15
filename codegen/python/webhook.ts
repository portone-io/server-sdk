import * as path from "@std/path"
import { toSnakeCase } from "../common/casing.ts"
import { Definition } from "../common/webhook/definition.ts"
import { filterName, PythonWriter } from "./common.ts"
import { annotateDescription, writeDescription } from "./description.ts"

export function generateEntity(
  packagePath: string,
  definition: Definition,
) {
  const crossRef = new Set<string>()
  const std = new Set<string>([
    "__future__.annotations",
    "typing.Any",
    "typing.Optional",
  ])
  const writer = PythonWriter()
  const name = definition.name
  switch (definition.type) {
    case "object": {
      if (definition.interface) {
        const { coproduct, open } = definition.interface
        if (open) {
          writer.writeLine(`${name} = Union[${coproduct.join(", ")}, dict]`)
        } else {
          writer.writeLine(`${name} = Union[${coproduct.join(", ")}]`)
        }
        std.add("typing.Union")
        for (const variant of definition.interface.coproduct) {
          crossRef.add(
            `${toSnakeCase(variant)}.${variant}, _deserialize_${
              toSnakeCase(variant)
            }`,
          )
        }
        break
      }
      writer.writeLine("@dataclass")
      writer.writeLine(`class ${name}:`)
      writer.indent()
      writeDescription(
        writer,
        annotateDescription(definition.description ?? "", definition),
      )
      const properties = definition.properties.filter(({ required }) =>
        required
      ).concat(definition.properties.filter(({ required }) => !required))
        .filter(({ type }) => type !== "discriminant")
      if (properties.length === 0) {
        writer.writeLine("pass")
      }
      for (const property of properties) {
        const wrapOptional = (type: string): string => {
          if (!property.required) {
            return `Optional[${type}]`
          }
          return type
        }
        const name = filterName(property.name)
        switch (property.type) {
          case "discriminant":
            break
          case "string":
            writer.writeLine(`${name}: ${wrapOptional("str")}`)
            break
          case "integer":
            writer.writeLine(`${name}: ${wrapOptional("int")}`)
            break
          case "ref":
            writer.writeLine(
              `${name}: ${wrapOptional(property.value)}`,
            )
            crossRef.add(
              `${toSnakeCase(property.value)}.${property.value}, _deserialize_${
                toSnakeCase(property.value)
              }`,
            )
            break
          case "object":
            if (property.properties.length !== 0) {
              throw new Error(
                "properties with their properties specified are not supported",
                { cause: { definition } },
              )
            }
            writer.writeLine(`${name}: ${wrapOptional("dict")}`)
            break
        }
        writeDescription(
          writer,
          annotateDescription(property.description ?? "", property),
        )
      }
      writer.outdent()
      break
    }
    case "string":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  const sortedStd = [...std].toSorted()
  const stdGroups: { moduleName: string; names: string[] }[] = []
  for (const std of sortedStd) {
    const dot = std.lastIndexOf(".")
    const moduleName = std.slice(0, dot)
    const name = std.slice(dot + 1)
    const lastModule = stdGroups.at(-1)
    if (lastModule?.moduleName !== moduleName) {
      stdGroups.push({
        moduleName,
        names: [name],
      })
    } else {
      lastModule.names.push(name)
    }
  }
  const stdImports = stdGroups.map(({ moduleName, names }) =>
    `from ${moduleName} import ${names.join(", ")}`
  )
  const sortedRef = [...crossRef].toSorted()
  const refImports = sortedRef.map((ref) => {
    const dot = ref.lastIndexOf(".")
    const module = ref.slice(0, dot)
    const name = ref.slice(dot + 1)
    return `from .${module} import ${name}`
  })
  const imports = stdImports.concat(
    definition.type === "object"
      ? "from dataclasses import dataclass, field"
      : [],
  ).concat(refImports).join("\n")
  const content = (imports.length > 0 ? [imports] : []).concat(writer.content)
    .concat(generateDeserializeEntity(definition))
    .join("\n\n")
  const entityPath = path.join(
    packagePath,
    `${toSnakeCase(definition.name)}.py`,
  )
  Deno.writeTextFileSync(entityPath, content)
}

function generateDeserializeEntity(
  definition: Definition,
) {
  const writer = PythonWriter()
  writer.writeLine(
    `def _deserialize_${
      toSnakeCase(definition.name)
    }(obj: Any) -> ${definition.name}:`,
  )
  writer.indent()
  const checkType = (type: string, value: string = "obj") => {
    writer.writeLine(`if not isinstance(${value}, ${type}):`)
    writer.indent()
    writer.writeLine(`raise ValueError(f"{repr(${value})} is not ${type}")`)
    writer.outdent()
  }
  const checkKey = (key: string) => {
    writer.writeLine(`if "${key}" not in obj:`)
    writer.indent()
    writer.writeLine(`raise KeyError(f"'${key}' is not in {obj}")`)
    writer.outdent()
  }
  switch (definition.type) {
    case "object": {
      checkType("dict")
      if (definition.interface) {
        const { coproduct, open } = definition.interface
        for (const variant of coproduct) {
          writer.writeLine("try:")
          writer.indent()
          writer.writeLine(`return _deserialize_${toSnakeCase(variant)}(obj)`)
          writer.outdent()
          writer.writeLine("except Exception:")
          writer.indent()
          writer.writeLine("pass")
          writer.outdent()
        }
        if (open) {
          writer.writeLine(`return obj`)
        } else {
          writer.writeLine(
            `raise ValueError(f"{obj} is not ${definition.name}")`,
          )
        }
        break
      }
      const allProperties = []
      const properties = definition.properties.filter(({ required }) =>
        required
      ).concat(definition.properties.filter(({ required }) => !required))
      for (const property of properties) {
        const name = filterName(property.name)
        if (property.required) {
          checkKey(property.name)
        } else {
          writer.writeLine(`if "${property.name}" in obj:`)
          writer.indent()
        }
        writer.writeLine(`${name} = obj["${property.name}"]`)
        switch (property.type) {
          case "discriminant":
            writer.writeLine(`if ${name} != "${property.value}":`)
            writer.indent()
            writer.writeLine(
              `raise ValueError(f"{repr(${name})} is not '${property.value}'")`,
            )
            writer.outdent()
            break
          case "string":
            checkType("str", name)
            allProperties.push(name)
            break
          case "integer":
            checkType("int", name)
            allProperties.push(name)
            break
          case "ref":
            writer.writeLine(
              `${name} = _deserialize_${toSnakeCase(property.value)}(${name})`,
            )
            allProperties.push(name)
            break
          case "object":
            checkType("dict", name)
            allProperties.push(name)
            break
        }
        if (!property.required) {
          writer.outdent()
          writer.writeLine("else:")
          writer.indent()
          writer.writeLine(`${name} = None`)
          writer.outdent()
        }
      }
      writer.writeLine(`return ${definition.name}(${allProperties.join(", ")})`)
      break
    }
    case "string":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  writer.outdent()
  return writer.content
}
