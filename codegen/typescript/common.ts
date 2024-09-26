import type { Definition } from "../parser/definition.ts"

export function intoInlineTypeName(definition: Definition): string {
  switch (definition.type) {
    case "string":
      return "string"
    case "number":
    case "integer":
      return "number"
    case "boolean":
      return "boolean"
    case "ref":
      return definition.value
    case "oneOf":
      return definition.variants.map(({ name }) => name).join(" | ")
    case "discriminant":
      return `"${definition.value}"`
    case "enum":
      return definition.variants.map(({ value }) => `"${value}"`).join(" | ")
    case "array":
      return `${intoInlineTypeName(definition.item)}[]`
    case "object":
      throw new Error("unsupported inline type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
}
