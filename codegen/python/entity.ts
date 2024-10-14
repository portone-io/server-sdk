import * as path from "@std/path"
import type { Definition } from "../parser/definition.ts"
import { filterName, PythonWriter, toSnakeCase } from "./common.ts"
import { annotateDescription, writeDescription } from "./description.ts"

export function generateEntity(
  packagePath: string,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
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
      writer.writeLine("@dataclass")
      if (definition.additionalProperties) {
        const additionalDefinition = entityMap.get(
          definition.additionalProperties,
        )
        if (!additionalDefinition) {
          throw new Error("unrecognized additional properties", {
            cause: { additionalProperties: definition.additionalProperties },
          })
        }
        if (additionalDefinition.type !== "object") {
          throw new Error("unsupported additional properties type", {
            cause: { additionalDefinition },
          })
        }
        writer.writeLine(
          `class ${name}(${definition.additionalProperties}):`,
        )
        crossRef.add(definition.additionalProperties)
      } else {
        writer.writeLine(`class ${name}:`)
      }
      writer.indent()
      writeDescription(
        writer,
        annotateDescription(definition.description ?? "", definition),
      )
      const properties = definition.properties.filter(({ required }) =>
        required
      ).concat(definition.properties.filter(({ required }) => !required))
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
            std.add("typing.Literal")
            writer.writeLine(
              `${name}: Literal["${property.value}"] = field(repr=False)`,
            )
            break
          case "string":
            writer.writeLine(`${name}: ${wrapOptional("str")}`)
            break
          case "boolean":
            writer.writeLine(`${name}: ${wrapOptional("bool")}`)
            break
          case "number":
            writer.writeLine(`${name}: ${wrapOptional("float")}`)
            break
          case "integer":
            writer.writeLine(`${name}: ${wrapOptional("int")}`)
            break
          case "ref":
            writer.writeLine(
              `${name}: ${wrapOptional(property.value)}`,
            )
            crossRef.add(property.value)
            break
          case "array":
            switch (property.item.type) {
              case "string":
                writer.writeLine(
                  `${name}: ${wrapOptional("list[str]")}`,
                )
                break
              case "boolean":
                writer.writeLine(
                  `${name}: ${wrapOptional("list[bool]")}`,
                )
                break
              case "number":
                writer.writeLine(
                  `${name}: ${wrapOptional("list[float]")}`,
                )
                break
              case "integer":
                writer.writeLine(
                  `${name}: ${wrapOptional("list[int]")}`,
                )
                break
              case "ref":
                writer.writeLine(
                  `${name}: ${wrapOptional(`list[${property.item.value}]`)}`,
                )
                crossRef.add(property.item.value)
                break
              case "discriminant":
              case "object":
              case "oneOf":
              case "enum":
              case "array":
                throw new Error("unsupported array item type", {
                  cause: { definition },
                })
              default:
                throw new Error("unrecognized definition type", {
                  cause: { definition },
                })
            }
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
          case "enum":
          case "oneOf":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
        }
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        writeDescription(writer, annotateDescription(description, property))
      }
      writer.outdent()
      break
    }
    case "oneOf": {
      if (definition.variants.length > 1) {
        const variants = definition.variants.map(({ name }) => name).join(", ")
        writer.writeLine(
          `${name} = Union[${variants}]`,
        )
        std.add("typing.Union")
      } else {
        writer.writeLine(`${name} = ${definition.variants[0].name}`)
      }
      writeDescription(
        writer,
        annotateDescription(definition.description ?? "", definition),
      )
      for (const variant of definition.variants) {
        crossRef.add(variant.name)
      }
      break
    }
    case "enum": {
      const variants = definition.variants.map(({ value }) => `"${value}"`)
        .join(", ")
      writer.writeLine(
        `${name} = Literal[${variants}]`,
      )
      std.add("typing.Literal")
      writeDescription(
        writer,
        annotateDescription(definition.description ?? "", definition),
      )
      break
    }
    case "string":
    case "boolean":
    case "number":
    case "integer":
    case "array":
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
    const path = categoryMap.get(ref)?.split(".").map((name) =>
      toSnakeCase(name)
    ).join(".")
    if (!path) {
      throw new Error("unrecognized reference", { cause: { definition } })
    }
    return `from portone_server_sdk._generated.${path}.${
      toSnakeCase(ref)
    } import ${ref}, _deserialize_${toSnakeCase(ref)}, _serialize_${
      toSnakeCase(ref)
    }`
  })
  const imports = stdImports.concat(
    definition.type === "object"
      ? "from dataclasses import dataclass, field"
      : [],
  ).concat(refImports).join("\n")
  const content = (imports.length > 0 ? [imports] : []).concat(writer.content)
    .concat(generateSerializeEntity(definition))
    .concat(generateDeserializeEntity(definition, entityMap))
    .join("\n\n")
  const entityPath = path.join(
    packagePath,
    `${toSnakeCase(definition.name)}.py`,
  )
  Deno.writeTextFileSync(entityPath, content)
}

function generateDeserializeEntity(
  definition: Definition,
  entityMap: Map<string, Definition>,
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
      const allProperties = []
      if (definition.additionalProperties) {
        const additionalDefinition = entityMap.get(
          definition.additionalProperties,
        )
        if (!additionalDefinition) {
          throw new Error("unrecognized additional properties", {
            cause: { additionalProperties: definition.additionalProperties },
          })
        }
        if (additionalDefinition.type !== "object") {
          throw new Error("unsupported additional properties type", {
            cause: { additionalDefinition },
          })
        }
        writer.writeLine(
          `additional = _deserialize_${
            toSnakeCase(definition.additionalProperties)
          }(obj)`,
        )
        for (const property of additionalDefinition.properties) {
          writer.writeLine(
            `${filterName(property.name)} = additional.${
              filterName(property.name)
            }`,
          )
          allProperties.push(filterName(property.name))
        }
      }
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
            break
          case "boolean":
            checkType("bool", name)
            break
          case "number":
            checkType("(float, int)", name)
            break
          case "integer":
            checkType("int", name)
            break
          case "ref":
            writer.writeLine(
              `${name} = _deserialize_${toSnakeCase(property.value)}(${name})`,
            )
            break
          case "array":
            checkType("list", name)
            writer.writeLine(`for i, item in enumerate(${name}):`)
            writer.indent()
            switch (property.item.type) {
              case "string":
                checkType("str", "item")
                break
              case "boolean":
                checkType("bool", "item")
                break
              case "number":
                checkType("(float, int)", "item")
                break
              case "integer":
                checkType("int", "item")
                break
              case "ref":
                writer.writeLine(
                  `item = _deserialize_${
                    toSnakeCase(property.item.value)
                  }(item)`,
                )
                writer.writeLine(`${name}[i] = item`)
                break
              case "discriminant":
              case "object":
              case "oneOf":
              case "enum":
              case "array":
                throw new Error("unsupported array item type", {
                  cause: { definition },
                })
              default:
                throw new Error("unrecognized definition type", {
                  cause: { definition },
                })
            }
            writer.outdent()
            break
          case "object":
            checkType("dict", name)
            break
          case "enum":
          case "oneOf":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
        }
        if (!property.required) {
          writer.outdent()
          writer.writeLine("else:")
          writer.indent()
          writer.writeLine(`${name} = None`)
          writer.outdent()
        }
        allProperties.push(name)
      }
      writer.writeLine(`return ${definition.name}(${allProperties.join(", ")})`)
      break
    }
    case "oneOf": {
      for (const variant of definition.variants) {
        writer.writeLine("try:")
        writer.indent()
        writer.writeLine(
          `return _deserialize_${toSnakeCase(variant.name)}(obj)`,
        )
        writer.outdent()
        writer.writeLine("except Exception:")
        writer.indent()
        writer.writeLine("pass")
        writer.outdent()
      }
      writer.writeLine(
        `raise ValueError(f"{repr(obj)} is not ${definition.name}")`,
      )
      break
    }
    case "enum": {
      const variants = definition.variants.map(({ value }) => `"${value}"`)
        .join(", ")
      writer.writeLine(`if obj not in [${variants}]:`)
      writer.indent()
      writer.writeLine(
        `raise ValueError(f"{repr(obj)} is not ${definition.name}")`,
      )
      writer.outdent()
      writer.writeLine("return obj")
      break
    }
    case "string":
    case "boolean":
    case "number":
    case "integer":
    case "array":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  writer.outdent()
  return writer.content
}

function generateSerializeEntity(definition: Definition) {
  const writer = PythonWriter()
  writer.writeLine(
    `def _serialize_${
      toSnakeCase(definition.name)
    }(obj: ${definition.name}) -> Any:`,
  )
  writer.indent()
  switch (definition.type) {
    case "enum":
      writer.writeLine("return obj")
      break
    case "object": {
      if (definition.additionalProperties) {
        writer.writeLine(
          `entity = _serialize_${
            toSnakeCase(definition.additionalProperties)
          }(obj)`,
        )
      } else {
        writer.writeLine("entity = {}")
      }
      const properties = definition.properties.filter(({ required }) =>
        required
      ).concat(definition.properties.filter(({ required }) => !required))
      for (const property of properties) {
        const name = filterName(property.name)
        if (!property.required) {
          writer.writeLine(`if obj.${name} is not None:`)
          writer.indent()
        }
        switch (property.type) {
          case "string":
          case "discriminant":
          case "boolean":
          case "number":
          case "integer":
          case "object":
            writer.writeLine(`entity["${property.name}"] = obj.${name}`)
            break
          case "ref":
            writer.writeLine(
              `entity["${property.name}"] = _serialize_${
                toSnakeCase(property.value)
              }(obj.${name})`,
            )
            break
          case "array":
            switch (property.item.type) {
              case "string":
              case "boolean":
              case "number":
              case "integer":
                writer.writeLine(`entity["${property.name}"] = obj.${name}`)
                break
              case "ref":
                writer.writeLine(
                  `entity["${property.name}"] = list(map(_serialize_${
                    toSnakeCase(property.item.value)
                  }, obj.${name}))`,
                )
                break
              case "discriminant":
              case "object":
              case "oneOf":
              case "enum":
              case "array":
                throw new Error("unsupported array item type", {
                  cause: { definition },
                })
              default:
                throw new Error("unrecognized definition type", {
                  cause: { definition },
                })
            }
            break
          case "enum":
          case "oneOf":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
        }
        if (!property.required) writer.outdent()
      }
      writer.writeLine("return entity")
      break
    }
    case "oneOf": {
      for (const variant of definition.variants) {
        writer.writeLine(
          `if obj.${filterName(variant.property)} == "${variant.value}":`,
        )
        writer.indent()
        writer.writeLine(`return _serialize_${toSnakeCase(variant.name)}(obj)`)
        writer.outdent()
      }
      break
    }
    case "string":
    case "boolean":
    case "number":
    case "integer":
    case "array":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  return writer.content
}
