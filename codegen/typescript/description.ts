import { Writer } from "../common/writer.ts"
import { Definition } from "../parser/definition.ts"

export function writeDescription(writer: Writer, description: string | null) {
  const trimmed = (description ?? "").trim()
  if (trimmed.length === 0) return
  const lines = trimmed.split("\n")
  if (lines.length === 1) {
    writer.writeLine(`/** ${lines[0]} */`)
  } else {
    writer.writeLine("/**")
    for (const line of lines) {
      writer.writeLine(" * " + line)
    }
    writer.writeLine(" */")
  }
}

export function annotateDescription(
  description: string,
  definition: Definition,
): string | null {
  if ("format" in definition) {
    switch (definition.format) {
      case null:
      case "double":
        return description
      case "int32":
      case "int64":
        return description.trimEnd() + `\n(${definition.format})`
      case "date-time":
        return description.trimEnd() + `\n(RFC 3339 date-time)`
      default:
        throw new Error("unrecognized type format", { cause: { definition } })
    }
  }
  return description
}
