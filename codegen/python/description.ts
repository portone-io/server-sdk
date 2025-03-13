import type { Writer } from "../common/writer.ts"
import { Annotated } from "../parser/common.ts"

export function writeDescription(writer: Writer, description: string | null) {
  const trimmed = (description ?? "").trim()
  if (trimmed.length === 0) return
  const lines = trimmed.split("\n")
  let first = true
  for (const line of lines) {
    if (first) {
      first = false
      writer.writeLine(`"""${line}`)
    } else {
      writer.writeLine(`${line}`)
    }
  }
  writer.writeLine(`"""`)
}

export function annotateDescription(
  description: string,
  definition: Annotated,
): string {
  if ("format" in definition) {
    switch (definition.format) {
      case null:
      case "double":
        return description
      case "date":
        return [description?.trimEnd() ?? []].flat().concat(
          `(yyyy-MM-dd)`,
        ).join("\n")
      case "date-time":
        return [description?.trimEnd() ?? []].flat().concat(
          `(RFC 3339 date-time)`,
        ).join("\n")
      case "int32":
      case "int64":
        return [description?.trimEnd() ?? []].flat().concat(
          `(${definition.format})`,
        ).join("\n")
      default:
        throw new Error("unrecognized type format", { cause: { definition } })
    }
  }
  return description
}
