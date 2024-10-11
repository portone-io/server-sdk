import type { Writer } from "../common/writer.ts"

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
