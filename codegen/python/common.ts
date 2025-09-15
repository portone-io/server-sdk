import { toSnakeCase } from "../common/casing.ts"
import { Writer } from "../common/writer.ts"
import type { Definition } from "../parser/definition.ts"

export function intoInlineTypeName(definition: Definition): string {
  switch (definition.type) {
    case "string":
      return "str"
    case "number":
      return "float"
    case "integer":
      return "int"
    case "boolean":
      return "bool"
    case "ref":
      return definition.value
    case "oneOf":
      return `Union[${definition.variants.map(({ name }) => name).join(", ")}]`
    case "discriminant":
      return `Literal["${definition.value}"]`
    case "enum":
      return `Literal[${
        definition.variants.map(({ value }) => `"${value}"`).join(", ")
      }]`
    case "array":
      return `list[${intoInlineTypeName(definition.item)}]`
    case "object":
      if (definition.properties.length !== 0) {
        throw new Error("unsupported inline definition object type", {
          cause: { definition },
        })
      }
      return "dict"
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
}

export function PythonWriter() {
  return Writer(" ".repeat(4))
}

const keywords = new Set([
  "False",
  "await",
  "else",
  "import",
  "pass",
  "None",
  "break",
  "except",
  "in",
  "raise",
  "True",
  "class",
  "finally",
  "is",
  "return",
  "and",
  "continue",
  "for",
  "lambda",
  "try",
  "as",
  "def",
  "from",
  "nonlocal",
  "while",
  "assert",
  "del",
  "global",
  "not",
  "with",
  "async",
  "elif",
  "if",
  "or",
  "yield",
])
export function filterName(name: string): string {
  const snakeCase = toSnakeCase(name)
  return keywords.has(snakeCase) ? `${snakeCase}_` : snakeCase
}
