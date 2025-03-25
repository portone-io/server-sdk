import { Package } from "../parser/openapi.ts"

export function isClientPackage(pack: Package) {
  return pack.operations.length > 0 || pack.subpackages.length > 0
}
