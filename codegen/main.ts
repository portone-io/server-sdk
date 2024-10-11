import { Command } from "@cliffy/command"
import * as path from "@std/path"
import * as kotlin from "./kotlin/project.ts"
import { packageSchema } from "./parser/openapi.ts"
import * as python from "./python/project.ts"
import { updatePackageJson } from "./typescript/packaging.ts"
import * as typescript from "./typescript/project.ts"

if (import.meta.main) {
  await new Command()
    .name("server-sdk-codegen")
    .arguments("[language:string]")
    .action((options, ...args) => {
      const packages = packageSchema()
      switch (args[0]) {
        case "javascript":
        case "typescript":
        case "ts":
        case "js": {
          const jsRoot = path.fromFileUrl(import.meta.resolve("../javascript"))
          const entrypoints = typescript.generateProject(
            jsRoot,
            packages,
          )
          updatePackageJson(jsRoot, entrypoints)
          break
        }
        case "python":
        case "py": {
          const pyRoot = path.fromFileUrl(import.meta.resolve("../python"))
          python.generateProject(pyRoot, packages)
          break
        }
        case "jvm":
        case "java":
        case "kotlin":
        case "kt": {
          const kotlinRoot = path.fromFileUrl(import.meta.resolve("../jvm"))
          kotlin.generateProject(kotlinRoot, packages)
          break
        }
        default:
          throw new Error("unrecognized language", {
            cause: { language: args[0] },
          })
      }
    })
    .parse(Deno.args)
}
