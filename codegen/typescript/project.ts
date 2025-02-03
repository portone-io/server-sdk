import * as fs from "@std/fs"
import * as path from "@std/path"
import { toCamelCase, toPascalCase } from "@std/text"
import { makeCategoryMap, makeEntityMap } from "../common/maps.ts"
import {
  entities as webhookEntities,
  types as webhookTypes,
} from "../common/webhook.ts"
import type { Definition } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"
import { TypescriptWriter } from "./common.ts"
import { generateEntity } from "./entity.ts"
import { writeOperation } from "./operation.ts"
import { generateEntity as generateWebhookEntity } from "./webhook.ts"

/**
 * @returns entrypoints
 */
export function generateProject(projectRoot: string, pack: Package): string[] {
  const srcPath = path.join(projectRoot, "src/generated")
  if (fs.existsSync(srcPath)) Deno.removeSync(srcPath, { recursive: true })
  fs.ensureDirSync(srcPath)
  const categoryMap = makeCategoryMap(pack)
  const entityMap = makeEntityMap(pack)
  const oneOfErrors = new Set<string>()
  collectErrors(pack, entityMap, oneOfErrors, new Set())
  generateEntityDirectory(srcPath, pack, categoryMap, ".", oneOfErrors)
  generateWebhook(srcPath)
  const allClients: Client[] = []
  generateClient(
    srcPath,
    pack,
    "..",
    ".",
    categoryMap,
    entityMap,
    allClients,
  )
  allClients.sort((a, b) => a.name.localeCompare(b.name))
  generateIndex(srcPath, pack, allClients)
  generateCategoryIndex(
    srcPath,
    pack,
    categoryMap,
    entityMap,
    oneOfErrors,
    0,
    "",
    "PortOneError",
  )
  const entrypoints = [
    ...categoryMap.values(),
  ].map((category) => category.replace(".", "/"))
  entrypoints.sort()
  return entrypoints
}

function generateIndex(srcPath: string, pack: Package, clients: Client[]) {
  const writer = TypescriptWriter()
  writer.writeLine(`export { RestError } from "./RestError"`)
  for (const subpackage of pack.subpackages) {
    writer.writeLine(
      `export * as ${toCamelCase(subpackage.category)} from "./${
        toCamelCase(subpackage.category)
      }"`,
    )
  }
  for (const client of clients) {
    writer.writeLine(
      `export { ${client.name} } from "${client.hierarchy}/client"`,
    )
  }
  Deno.writeTextFileSync(path.join(srcPath, "index.ts"), writer.content)
}

function generateWebhook(srcPath: string) {
  const webhookPath = path.join(srcPath, "webhook")
  fs.ensureDirSync(webhookPath)
  const writer = TypescriptWriter()
  for (
    const entity of webhookEntities.toSorted((a, b) =>
      a.name.localeCompare(b.name)
    )
  ) {
    const entityPath = path.join(webhookPath, `${entity.name}.ts`)
    Deno.writeTextFileSync(entityPath, generateWebhookEntity(entity))
    writer.writeLine(
      `export type { ${entity.name} } from "./${entity.name}"`,
    )
  }
  writer.writeLine(`import type { Webhook } from "./Webhook"`)
  writer.writeLine(
    `import type { Unrecognized } from "../../utils/unrecognized"`,
  )
  writer.writeLine("")
  writer.writeLine(
    `export function isUnrecognizedWebhook(entity: Webhook): entity is { readonly type: Unrecognized } {`,
  )
  writer.indent()
  let first = true
  for (const [type] of webhookTypes) {
    if (first) {
      writer.writeLine(`return entity.type !== "${type}"`)
      writer.indent()
      first = false
    } else {
      writer.writeLine(`&& entity.type !== "${type}"`)
    }
  }
  writer.outdent()
  writer.outdent()
  writer.writeLine(`}`)
  Deno.writeTextFileSync(path.join(webhookPath, "index.ts"), writer.content)
}

function collectErrors(
  pack: Package,
  entityMap: Map<string, Definition>,
  oneOfErrors: Set<string>,
  variantErrors: Set<string>,
) {
  for (const operation of pack.operations) {
    oneOfErrors.add(operation.errors)
    const errorEntity = entityMap.get(operation.errors)
    if (!errorEntity) {
      throw new Error("unrecognized error", { cause: { operation } })
    }
    switch (errorEntity.type) {
      case "object":
        variantErrors.add(errorEntity.name)
        break
      case "oneOf":
        for (const variant of errorEntity.variants) {
          variantErrors.add(variant.name)
        }
        break
      case "string":
      case "number":
      case "boolean":
      case "ref":
      case "discriminant":
      case "enum":
      case "array":
      case "integer":
        continue
      default:
        throw new Error("unrecognized error type", {
          cause: { error: errorEntity },
        })
    }
  }
  for (const subpackage of pack.subpackages) {
    collectErrors(subpackage, entityMap, oneOfErrors, variantErrors)
  }
}

type Client = {
  hierarchy: string
  name: string
}

function generateClient(
  packagePath: string,
  pack: Package,
  hierarchyToSrc: string,
  hierarchy: string,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
  collected: Client[],
): Client | null {
  let client = null
  const hasClient = pack.subpackages.length > 0 || pack.operations.length > 0
  if (hasClient) {
    const error = `${toPascalCase(pack.category)}Error`
    const importWriter = TypescriptWriter()
    const typeWriter = TypescriptWriter()
    const errorWriter = TypescriptWriter()
    const writer = TypescriptWriter()
    if (pack.operations.length > 0) {
      importWriter.writeLine(`import { ${error} } from "./${error}"`)
      importWriter.writeLine(
        `import type { Unrecognized } from "./${hierarchyToSrc}/utils/unrecognized"`,
      )
      importWriter.writeLine(
        `import { USER_AGENT, type PortOneClientInit } from "${hierarchyToSrc}/client"`,
      )
    } else {
      importWriter.writeLine(
        `import type { PortOneClientInit } from "${hierarchyToSrc}/client"`,
      )
    }
    const clientName = pack.category === "root"
      ? "PortOneClient"
      : `${toPascalCase(pack.category)}Client`
    client = {
      hierarchy,
      name: clientName,
    }
    collected.push(client)
    writer.writeLine("/**")
    writer.writeLine(" * 포트원 API 클라이언트를 생성합니다.")
    writer.writeLine(" */")
    writer.writeLine(
      `export function ${clientName}(init: PortOneClientInit): ${clientName} {`,
    )
    writer.indent()
    if (pack.operations.length > 0) {
      writer.writeLine(
        `const baseUrl = init.baseUrl ?? "https://api.portone.io"`,
      )
      writer.writeLine(`const secret = init.secret`)
    }
    writer.writeLine("return {")
    writer.indent()
    typeWriter.writeLine(`export type ${clientName} = {`)
    typeWriter.indent()
    const crossRef = new Set<string>()
    for (const operation of pack.operations) {
      writeOperation(
        writer,
        typeWriter,
        errorWriter,
        operation,
        entityMap,
        crossRef,
        error,
      )
    }
    for (const subpackage of pack.subpackages) {
      const subclient = generateClient(
        `${packagePath}/${toCamelCase(subpackage.category)}`,
        subpackage,
        `../${hierarchyToSrc}`,
        `${hierarchy}/${subpackage.category}`,
        categoryMap,
        entityMap,
        collected,
      )
      if (subclient) {
        importWriter.writeLine(
          `import { ${subclient.name} } from "./${subpackage.category}/client"`,
        )
        writer.writeLine(
          `${toCamelCase(subpackage.category)}: ${subclient.name}(init),`,
        )
        typeWriter.writeLine(
          `${toCamelCase(subpackage.category)}: ${subclient.name}`,
        )
      }
    }
    typeWriter.outdent()
    typeWriter.writeLine("}")
    writer.outdent()
    writer.writeLine("}")
    writer.outdent()
    writer.writeLine("}")
    for (const ref of [...crossRef].toSorted()) {
      const rename = ref
      let name = rename
      if (name.startsWith("_Internal")) {
        name = name.slice(9)
      }
      const category = categoryMap.get(name)
      if (!category) {
        throw new Error("unrecognized ref", { cause: { ref: name } })
      }
      if (name === rename) {
        importWriter.writeLine(
          `import type { ${name} } from "${hierarchyToSrc}/generated/${
            category.replaceAll(".", "/")
          }/${name}"`,
        )
      } else {
        importWriter.writeLine(
          `import type { ${name} as ${rename} } from "${hierarchyToSrc}/generated/${
            category.replaceAll(".", "/")
          }/${name}"`,
        )
      }
    }
    const operationPath = path.join(packagePath, "client.ts")
    Deno.writeTextFileSync(
      operationPath,
      importWriter.content + writer.content + typeWriter.content +
        errorWriter.content,
    )
  }
  return client
}

function generateEntityDirectory(
  packagePath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  hierarchy: string,
  exclude: Set<string>,
) {
  for (const entity of pack.entities) {
    if (exclude.has(entity.name)) continue
    const entityPath = path.join(packagePath, `${entity.name}.ts`)
    Deno.writeTextFileSync(
      entityPath,
      generateEntity(categoryMap, entity, hierarchy),
    )
  }
  for (const subpackage of pack.subpackages) {
    const subPath = path.join(packagePath, subpackage.category)
    fs.ensureDirSync(subPath)
    generateEntityDirectory(
      subPath,
      subpackage,
      categoryMap,
      hierarchy + "/..",
      exclude,
    )
  }
}

function generateCategoryIndex(
  packagePath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
  omitEntities: Set<string>,
  depth: number,
  canonicalCategory: string,
  parentError: string,
) {
  const writer = TypescriptWriter()
  const crossRef = new Set<string>()
  const error = pack.category === "root"
    ? "RestError"
    : `${toPascalCase(pack.category)}Error`
  if (
    pack.operations.length > 0 || pack.subpackages.length > 0
  ) {
    const errorWriter = TypescriptWriter()
    errorWriter.writeLine(
      `import type { Unrecognized } from "${
        "../".repeat(depth)
      }../utils/unrecognized"`,
    )
    errorWriter.writeLine(
      `import { ${parentError} } from "../${parentError}"`,
    )
    const variantErrors = new Set<string>()
    collectErrors(pack, entityMap, new Set(), variantErrors)
    const dataType = [...variantErrors]
    dataType.sort()
    for (const error of dataType) {
      const category = categoryMap.get(error)
      if (!category) {
        throw new Error("unrecognized error ref", { cause: error })
      }
      errorWriter.writeLine(
        `import type { ${error} } from "${
          depth === 0 ? "./" : "../".repeat(depth)
        }${category.replaceAll(".", "/")}/${error}"`,
      )
    }
    errorWriter.writeLine(
      `export abstract class ${error} extends ${parentError} {`,
    )
    errorWriter.indent()
    if (pack.category === "root") {
      errorWriter.writeLine(
        `readonly data: ${
          dataType.join(" | ")
        } | { readonly type: Unrecognized }`,
      )
      errorWriter.writeLine("/** @ignore */")
      errorWriter.writeLine(
        `constructor(data: ${
          dataType.join(" | ")
        } | { readonly type: Unrecognized }) {`,
      )
      errorWriter.indent()
      errorWriter.writeLine(
        `const message = "message" in data ? data.message : undefined`,
      )
      errorWriter.writeLine("super(message)")
      errorWriter.writeLine("this.data = data")
      errorWriter.outdent()
      errorWriter.writeLine(`}`)
    } else {
      errorWriter.writeLine(
        `declare readonly data: ${
          dataType.join(" | ")
        } | { readonly type: Unrecognized }`,
      )
    }
    errorWriter.outdent()
    errorWriter.writeLine(`}`)
    Deno.writeTextFileSync(
      path.join(packagePath, `${error}.ts`),
      errorWriter.content,
    )
    writer.writeLine(`export { ${error} } from "./${error}"`)
  }
  for (const entity of pack.entities) {
    if (omitEntities.has(entity.name)) continue
    writer.writeLine(`export * from "./${entity.name}"`)
  }
  if (pack.operations.length > 0) {
    writer.writeLine(
      `export * from "./client"`,
    )
  }
  for (const subpackage of pack.subpackages) {
    const subPath = path.join(packagePath, subpackage.category)
    fs.ensureDirSync(subPath)
    generateCategoryIndex(
      subPath,
      subpackage,
      categoryMap,
      entityMap,
      omitEntities,
      depth + 1,
      `${canonicalCategory}/${subpackage.category}`,
      error,
    )
    writer.writeLine(
      `export * as ${toCamelCase(subpackage.category)} from "./${
        toCamelCase(subpackage.category)
      }"`,
    )
  }
  const sortedRef = [...crossRef].toSorted()
  const importWriter = TypescriptWriter()
  for (const ref of sortedRef) {
    const category = categoryMap.get(ref)
    if (!category) {
      throw new Error("unrecognized category", { cause: { ref } })
    }
    importWriter.writeLine(
      `import type { ${ref} } from "${"../".repeat(depth)}/${
        category.split(".").join("/")
      }/${ref}"`,
    )
  }
  for (const subpackage of pack.subpackages) {
    importWriter.writeLine(
      `import * as ${
        toPascalCase(subpackage.category)
      } from "./${subpackage.category}"`,
    )
  }
  if (pack.category !== "root") {
    const indexPath = path.join(packagePath, "index.ts")
    Deno.writeTextFileSync(indexPath, importWriter.content + writer.content)
  }
}
