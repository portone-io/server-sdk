export function Writer() {
  return {
    content: "",
    level: 0,
    indent() {
      this.level += 1
    },
    outdent() {
      this.level -= 1
    },
    writeLine(line: string) {
      this.content += ("\t".repeat(this.level) + line).trimEnd()
      this.content += "\n"
    },
  }
}
export type Writer = ReturnType<typeof Writer>
