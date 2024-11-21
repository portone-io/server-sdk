import * as fs from "@std/fs"
import * as path from "@std/path"
import { toCamelCase, toPascalCase } from "@std/text"
import { makeCategoryMap, makeEntityMap } from "../common/maps.ts"
import { entities as webhookEntities } from "../common/webhook.ts"
import type { Definition } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"
import { intoInlineTypeName, TypescriptWriter } from "./common.ts"
import { writeDescription } from "./description.ts"
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
  const variantErrors = new Set<string>()
  collectErrors(pack, entityMap, oneOfErrors, variantErrors)
  generateErrors(srcPath, [...variantErrors].toSorted(), categoryMap, entityMap)
  generateEntityDirectory(srcPath, pack, categoryMap, ".")
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
  const omitEntities = oneOfErrors.union(variantErrors)
  generateCategoryIndex(
    srcPath,
    pack,
    categoryMap,
    entityMap,
    omitEntities,
    0,
    "",
  )
  const entrypoints = [
    ...categoryMap.values(),
  ].map((category) => category.replace(".", "/"))
  entrypoints.sort()
  return entrypoints
}

function generateIndex(srcPath: string, pack: Package, clients: Client[]) {
  const writer = TypescriptWriter()
  writer.writeLine(`export * as Errors from "./errors"`)
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
      `export type { ${entity.name} } from "./${entity.name}.ts"`,
    )
  }
  Deno.writeTextFileSync(path.join(webhookPath, "index.ts"), writer.content)
}

const PortOneError = `
export abstract class PortOneError extends Error {
  abstract readonly _tag: string;

  constructor(message?: string, options?: ErrorOptions) {
    super(message ?? "", options)
    Object.setPrototypeOf(this, PortOneError.prototype)
    this.name = "PortOneError"
    this.stack = new Error(message ?? "").stack
  }
}
  
export class UnknownError extends PortOneError {
  readonly _tag = "PortOneUnknownError"

  constructor(cause: unknown) {
    super("알 수 없는 에러가 발생했습니다.", { cause })
    Object.setPrototypeOf(this, UnknownError.prototype)
  }
}`

function generateErrors(
  srcPath: string,
  errors: string[],
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  const writer = TypescriptWriter()
  const crossRef = new Set<string>()
  for (const error of errors) {
    const path = categoryMap.get(error)?.replace(".", "/")
    if (!path) {
      throw new Error("unrecognized error reference", { cause: { error } })
    }
    const definition = entityMap.get(error)
    if (!definition) {
      throw new Error("unrecognized error reference", { cause: { error } })
    }
    if (definition.type !== "object") {
      throw new Error("unsupported generation of error type", {
        cause: { definition },
      })
    }
    for (const property of definition.properties) {
      switch (property.type) {
        case "ref":
          crossRef.add(property.value)
          break
        case "oneOf":
          for (const { name } of property.variants) {
            crossRef.add(name)
          }
          break
        case "array":
          switch (property.item.type) {
            case "ref":
              crossRef.add(property.item.value)
              break
            case "string":
            case "number":
            case "boolean":
            case "oneOf":
            case "discriminant":
            case "enum":
            case "integer":
              break
            case "object":
            case "array":
              throw new Error("unsupported error property array item type", {
                cause: { definition },
              })
            default:
              throw new Error("unsupported definition type", {
                cause: { definition: property.item },
              })
          }
          break
        case "string":
        case "number":
        case "boolean":
        case "discriminant":
        case "enum":
        case "integer":
          break
        case "object":
          throw new Error("unsupported error property type", {
            cause: { definition },
          })
      }
    }
    writer.writeLine(
      `import type { ${error} as Internal${error} } from "./${path}/${error}"`,
    )
  }
  const sortedRef = [...crossRef]
  sortedRef.sort()
  for (const ref of crossRef) {
    const path = categoryMap.get(ref)?.replace(".", "/")
    if (!path) {
      throw new Error("unrecognized error property reference", {
        cause: { ref },
      })
    }
    writer.writeLine(
      `import type { ${ref} } from "./${path}/${ref}"`,
    )
  }
  for (const line of PortOneError.split("\n")) {
    writer.writeLine(line)
  }
  for (const error of errors) {
    const definition = entityMap.get(error)
    if (!definition) {
      throw new Error("unrecognized error reference", { cause: { error } })
    }
    if (definition.type !== "object") {
      throw new Error("unsupported generation of error type", {
        cause: { definition },
      })
    }
    const additionalProperties = definition.properties.filter(({ name }) =>
      name !== "type" && name !== "message"
    )
    writer.writeLine("")
    writeDescription(writer, definition.description)
    writer.writeLine(`export class ${error} extends PortOneError {`)
    writer.indent()
    writer.writeLine(`readonly _tag = "PortOne${error}"`)
    for (const property of additionalProperties) {
      const name = property.required ? property.name : `${property.name}?`
      writer.writeLine(`readonly ${name}: ${intoInlineTypeName(property)}`)
    }
    writer.writeLine("")
    writer.writeLine("/** @ignore */")
    writer.writeLine(`constructor(error: Internal${error}) {`)
    writer.indent()
    if (definition.properties.some(({ name }) => name === "message")) {
      writer.writeLine("super(error.message)")
    } else {
      writer.writeLine("super()")
    }
    writer.writeLine(`Object.setPrototypeOf(this, ${error}.prototype)`)
    writer.writeLine(`this.name = "${error}"`)
    for (const { name } of additionalProperties) {
      writer.writeLine(`this.${name} = error.${name}`)
    }
    writer.outdent()
    writer.writeLine("}")
    writer.outdent()
    writer.writeLine("}")
  }
  const errorPath = path.join(srcPath, "errors.ts")
  Deno.writeTextFileSync(errorPath, writer.content)
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
    const importWriter = TypescriptWriter()
    const typeWriter = TypescriptWriter()
    const errorWriter = TypescriptWriter()
    const writer = TypescriptWriter()
    if (pack.operations.length > 0) {
      importWriter.writeLine(
        `import * as Errors from "${hierarchyToSrc}/generated/errors"`,
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
) {
  for (const entity of pack.entities) {
    const entityPath = path.join(packagePath, `${entity.name}.ts`)
    Deno.writeTextFileSync(
      entityPath,
      generateEntity(categoryMap, entity, hierarchy),
    )
  }
  for (const subpackage of pack.subpackages) {
    const subPath = path.join(packagePath, subpackage.category)
    fs.ensureDirSync(subPath)
    generateEntityDirectory(subPath, subpackage, categoryMap, hierarchy + "/..")
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
) {
  const crossRef = new Set<string>()
  const writer = TypescriptWriter()
  for (const entity of pack.entities) {
    if (omitEntities.has(entity.name)) continue
    writer.writeLine(`export type { ${entity.name} } from "./${entity.name}"`)
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
