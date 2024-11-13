import { Writer } from "../common/writer.ts"
import { Package } from "../parser/openapi.ts"

export function KotlinWriter() {
  return Writer(" ".repeat(2))
}

export function toPackageCase(name: string) {
  return name.split(".").map((s) => s.toLowerCase()).join(".")
}

export function toException(error: string) {
  return error.replace(/Error$/, "Exception")
}

const keywords = new Set(["operator", "in", "from"])
export function filterName(name: string) {
  if (keywords.has(name)) {
    return `\`${name}\``
  }
  return name
}

export function makeExtendsMap(
  pack: Package,
  extendsMap = new Map<string, Set<string>>(),
): Map<string, Set<string>> {
  for (const entity of pack.entities) {
    if (entity.type === "oneOf") {
      for (const variant of entity.variants) {
        let extension = extendsMap.get(variant.name)
        if (extension == null) {
          extension = new Set()
          extendsMap.set(variant.name, extension)
        }
        extension.add(entity.name)
      }
    }
  }
  for (const subpackage of pack.subpackages) {
    makeExtendsMap(subpackage, extendsMap)
  }
  return extendsMap
}
