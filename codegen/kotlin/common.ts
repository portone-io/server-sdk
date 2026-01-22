import { Writer } from "../common/writer.ts"

export function KotlinWriter() {
  return Writer(" ".repeat(2))
}

export function toPackageCase(name: string) {
  return name
    .split(".")
    .map((s) => s.toLowerCase())
    .join(".")
}

export function toException(error: string) {
  return error.replace(/Error$/, "Exception")
}

const keywords = new Set(["operator", "in"])
export function filterName(name: string) {
  if (keywords.has(name)) {
    return `\`${name}\``
  }
  return name
}

export type Extends = {
  parents: Set<string>
  properties: Set<string>
}
