import * as path from "@std/path"
export function updatePackageJson(rootPath: string, entrypoints: string[]) {
  const jsonPath = path.join(rootPath, "package.json")
  const json = JSON.parse(Deno.readTextFileSync(jsonPath))
  for (const entrypoint of entrypoints) {
    json.exports[`./${entrypoint}`] = `./src/generated/${entrypoint}/index.ts`
    json.publishConfig.exports[`./${entrypoint}`] = {
      types: `./dist/generated/${entrypoint}/index.d.ts`,
      require: `./dist/generated/${entrypoint}/index.cjs`,
      module: `./dist/generated/${entrypoint}/index.mjs`,
    }
  }
  Deno.writeTextFileSync(jsonPath, JSON.stringify(json, null, 2))
}
