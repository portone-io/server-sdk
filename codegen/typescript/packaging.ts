import * as path from "@std/path"
export function updatePackageJson(rootPath: string, entrypoints: string[]) {
  const jsonPath = path.join(rootPath, "package.json")
  const json = JSON.parse(Deno.readTextFileSync(jsonPath))
  json.publishConfig.imports = {
    "#generated/*": {
      types: "./dist/generated/*.d.ts",
      require: "./dist/generated/*.cjs",
      import: "./dist/generated/*.mjs",
    },
  }
  json.exports = {
    ".": "./src",
  }
  json.publishConfig.exports = {
    ".": {
      types: "./dist",
      require: "./dist",
      import: "./dist",
    },
  }
  for (const entrypoint of entrypoints) {
    json.exports[`./${entrypoint}`] = `./src/generated/${entrypoint}/index.ts`
    json.publishConfig.exports[`./${entrypoint}`] = {
      types: `./dist/generated/${entrypoint}/index.d.ts`,
      require: `./dist/generated/${entrypoint}/index.cjs`,
      import: `./dist/generated/${entrypoint}/index.mjs`,
    }
  }
  Deno.writeTextFileSync(jsonPath, JSON.stringify(json, null, 2))
}
