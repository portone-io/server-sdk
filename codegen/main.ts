import * as path from "@std/path"
import { packageSchema } from "./parser/openapi.ts"
import { generateProject } from "./typescript/project.ts"
import { updatePackageJson } from "./typescript/packaging.ts"

if (import.meta.main) {
  const packages = packageSchema()
  const jsRoot = path.fromFileUrl(import.meta.resolve("../javascript"))
  const entrypoints = generateProject(
    jsRoot,
    packages,
  )
  updatePackageJson(jsRoot, entrypoints)
}
