import type { Definition } from "../parser/definition.ts"
import { TypescriptWriter } from "./common.ts"
import { annotateDescription, writeDescription } from "./description.ts"

export function generateEntity(
  categoryMap: Map<string, string>,
  definition: Definition,
): string {
  const crossRef = new Set<string>()
  const writer = TypescriptWriter()
  writeDescription(
    writer,
    annotateDescription(definition.description ?? "", definition),
  )
  switch (definition.type) {
    case "string":
    case "boolean":
      writer.writeLine(`export type ${definition.name} = ${definition.type}`)
      break
    case "number":
    case "integer":
      writer.writeLine(`export type ${definition.name} = number`)
      break
    case "object":
      writer.writeLine(`export type ${definition.name} = {`)
      writer.indent()
      for (const property of definition.properties) {
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        writeDescription(writer, annotateDescription(description, property))
        const name = property.required ? property.name : `${property.name}?`
        switch (property.type) {
          case "discriminant":
            writer.writeLine(`${name}: "${property.value}"`)
            break
          case "string":
          case "boolean":
            writer.writeLine(`${name}: ${property.type}`)
            break
          case "number":
          case "integer":
            writer.writeLine(`${name}: number`)
            break
          case "ref":
            writer.writeLine(`${name}: ${property.value}`)
            crossRef.add(property.value)
            break
          case "array":
            switch (property.item.type) {
              case "string":
              case "boolean":
                writer.writeLine(`${name}: ${property.item.type}[]`)
                break
              case "number":
              case "integer":
                writer.writeLine(`${name}: number[]`)
                break
              case "ref":
                writer.writeLine(`${name}: ${property.item.value}[]`)
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
            writer.writeLine(`${name}: object`)
            break
          case "enum":
          case "oneOf":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
        }
      }
      writer.outdent()
      if (definition.additionalProperties) {
        crossRef.add(definition.additionalProperties)
        writer.writeLine(`} & ${definition.additionalProperties}`)
      } else {
        writer.writeLine("}")
      }
      break
    case "oneOf":
      writer.writeLine(`export type ${definition.name} =`)
      writer.indent()
      for (const { name, title } of definition.variants) {
        crossRef.add(name)
        writeDescription(writer, title)
        writer.writeLine(`| ${name}`)
      }
      writer.outdent()
      break
    case "enum":
      writer.writeLine(`export type ${definition.name} =`)
      writer.indent()
      for (const { value, title, description } of definition.variants) {
        const mergedDescription = [title ?? []].concat([description ?? []])
          .flat().join("\n\n")
        writeDescription(writer, mergedDescription)
        writer.writeLine(`| "${value}"`)
      }
      writer.outdent()
      break
    case "array":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  const sortedRef = [...crossRef]
  sortedRef.sort()
  const imports = sortedRef.map((ref) => {
    const path = categoryMap.get(ref)?.replace(".", "/")
    if (!path) {
      throw new Error("unrecognized reference", { cause: { definition } })
    }
    return `import type { ${ref} } from "#generated/${path}/${ref}"`
  })
  const content = imports.length > 0
    ? `${imports.join("\n")}\n\n${writer.content}`
    : writer.content
  return content
}
