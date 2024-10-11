import { Definition } from "../parser/definition.ts"
import { Package } from "../parser/openapi.ts"

export function makeCategoryMap(
  pack: Package,
  components: string[] = [],
  categoryMap: Map<string, string> = new Map(),
): Map<string, string> {
  for (const entity of pack.entities) {
    categoryMap.set(entity.name, components.join("."))
  }
  for (const subpackage of pack.subpackages) {
    components.push(subpackage.category)
    makeCategoryMap(subpackage, components, categoryMap)
    components.pop()
  }
  return categoryMap
}

export function makeEntityMap(
  pack: Package,
  entityMap: Map<string, Definition> = new Map(),
): Map<string, Definition> {
  for (const entity of pack.entities) {
    entityMap.set(entity.name, entity)
  }
  for (const subpackage of pack.subpackages) {
    makeEntityMap(subpackage, entityMap)
  }
  return entityMap
}
