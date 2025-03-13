import type { Writer } from "../common/writer.ts"
import { Annotated } from "../parser/common.ts"

export function writeDescription(writer: Writer, description: string | null) {
  const trimmed = (description ?? "").trim()
  if (trimmed.length === 0) return
  const lines = trimmed.split("\n")
  if (lines.length === 1) {
    writer.writeLine(`/** ${lines[0]} */`)
  } else {
    writer.writeLine("/**")
    for (const line of lines) {
      writer.writeLine(` * ${line}`)
    }
    writer.writeLine(" */")
  }
}

export function annotateDescription(
  description: string,
  definition: Annotated,
): string {
  if ("format" in definition) {
    switch (definition.format) {
      case null:
      case "double":
      case "int32":
      case "int64":
      case "date-time":
        return description
      case "date":
        return [description?.trimEnd() ?? []].flat().concat(
          "(yyyy-MM-dd)",
        ).join("\n")
      default:
        throw new Error("unrecognized type format", { cause: { definition } })
    }
  }
  return description
}
