import { Writer } from "../common/writer.ts"
import type { Definition } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"

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

export type Override = {
  properties: Set<string>
  from: Set<string>
}

export function makeOverridesMap(
  pack: Package,
  entityMap: Map<string, Definition>,
  overridesMap: Map<string, Override> = new Map(),
) {
  for (const entity of pack.entities) {
    if (entity.type !== "oneOf") continue
    const intersection = entity.variants.map((variant) => {
      const entity = entityMap.get(variant.name)
      if (entity?.type !== "object") {
        throw new Error("unsupported oneOf variant type", { cause: { entity } })
      }
      return new Set(
        entity.properties.map((property) =>
          `${property.name}/${property.required}/${
            property.type === "ref" ? property.value : property.type
          }`
        ),
      )
    }).reduce((a, b) => a.intersection(b))
    for (const variant of entity.variants) {
      let overrides = overridesMap.get(variant.name)
      if (!overrides) {
        overrides = {
          properties: new Set(),
          from: new Set(),
        }
        overridesMap.set(variant.name, overrides)
      }
      for (const property of intersection) {
        overrides.properties.add(property.split("/")[0])
      }
      overrides.from.add(entity.name)
    }
    overridesMap.set(entity.name, {
      properties: new Set(
        [...intersection].map((content) => content.split("/")[0]),
      ),
      from: new Set(entity.name),
    })
  }
  for (const subpackage of pack.subpackages) {
    makeOverridesMap(subpackage, entityMap, overridesMap)
  }
  return overridesMap
}
