import type { Definition } from "../common/webhook.ts"
import { TypescriptWriter } from "./common.ts"
import { annotateDescription, writeDescription } from "./description.ts"

export function generateEntity(
  definition: Definition,
): string {
  const crossRef = new Set<string>()
  const writer = TypescriptWriter()
  writeDescription(
    writer,
    annotateDescription(definition.description ?? "", definition),
  )
  switch (definition.type) {
    case "object":
      if (definition.interface) {
        writer.writeLine(`export type ${definition.name} =`)
        writer.indent()
        for (const variant of definition.interface.coproduct) {
          writer.writeLine(`| ${variant}`)
          crossRef.add(variant)
        }
        if (definition.interface.open) {
          writer.writeLine(
            `| { readonly ${definition.interface.discriminant}: unique symbol }`,
          )
        }
        writer.outdent()
        break
      }
      writer.writeLine(`export type ${definition.name} = {`)
      writer.indent()
      for (const property of definition.properties) {
        if (property.description) {
          writeDescription(
            writer,
            annotateDescription(property.description, property),
          )
        }
        const name = property.required ? property.name : `${property.name}?`
        switch (property.type) {
          case "discriminant":
            writer.writeLine(`${name}: "${property.value}"`)
            break
          case "string":
            writer.writeLine(`${name}: string`)
            break
          case "ref":
            writer.writeLine(`${name}: ${property.value}`)
            crossRef.add(property.value)
            break
          case "object":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
          default:
            throw new Error("unrecognized property type", {
              cause: { definition },
            })
        }
      }
      writer.outdent()
      writer.writeLine("}")
      break
    case "string":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  const sortedRef = [...crossRef]
  sortedRef.sort()
  const imports = sortedRef.map((ref) => {
    return `import type { ${ref} } from "./${ref}"`
  })
  const content = imports.length > 0
    ? `${imports.join("\n")}\n\n${writer.content}`
    : writer.content
  return content
}
