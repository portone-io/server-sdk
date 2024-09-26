import * as fs from "@std/fs"
import * as path from "@std/path"
import { toPascalCase } from "@std/text"
import { Writer } from "../common/writer.ts"
import type { Definition } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"
import { intoInlineTypeName } from "./common.ts"
import { writeDescription } from "./description.ts"
import { generateEntity } from "./entity.ts"
import { writeOperation } from "./operation.ts"

/**
 * @returns entrypoints
 */
export function generateProject(projectRoot: string, pack: Package): string[] {
  const srcPath = path.join(projectRoot, "src/generated")
  const categoryMap = makeCategoryMap(pack)
  const entityMap = makeEntityMap(pack)
  generateEntityDirectory(srcPath, pack, categoryMap)
  generateClient(srcPath, pack, categoryMap, entityMap)
  generateErrors(srcPath, pack, categoryMap, entityMap)
  generateIndex(srcPath, pack)
  const entrypoints = [...new Set(categoryMap.values())].map((category) =>
    category.replace(".", "/")
  )
  entrypoints.sort()
  return entrypoints
}

function generateIndex(srcPath: string, pack: Package) {
  const writer = Writer()
  writer.writeLine(`export * as Errors from "./errors"`)
  writer.writeLine(`export * from "./client"`)
  for (const subpackage of pack.subpackages) {
    writer.writeLine(
      `export * as ${
        toPascalCase(subpackage.category)
      } from "./${subpackage.category}"`,
    )
  }
  Deno.writeTextFileSync(path.join(srcPath, "index.ts"), writer.content)
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

  constructor(cause: never) {
    super("알 수 없는 에러가 발생했습니다.", { cause })
    Object.setPrototypeOf(this, UnknownError.prototype)
  }
}`

function generateErrors(
  srcPath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  const errors = collectErrors(pack)
  const writer = Writer()
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
      `import type { ${error} as Internal${error} } from "#generated/${path}/${error}"`,
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
    writer.writeLine(`import type { ${ref} } from "#generated/${path}/${ref}"`)
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

function collectErrors(pack: Package, errors: string[] = []): string[] {
  for (const entity of pack.entities) {
    if (!entity.name.endsWith("Error") || entity.type !== "object") continue
    errors.push(entity.name)
  }
  for (const subpackage of pack.subpackages) {
    collectErrors(subpackage, errors)
  }
  return errors
}

const PortOneClientInit = `
export type PortOneClientInit = {
  /**
	 * 포트원 API URL Origin
	 *
	 * 기본값은 \`https://api.portone.io\`입니다.
	 */
	baseUrl?: string;
	/**
	 * 상점 ID
	 */
	storeId?: string;
}`

function generateClient(
  srcPath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  const typeWriter = Writer()
  const writer = Writer()
  writer.writeLine(`import * as Errors from "./errors"`)
  for (
    const subpackage of pack.subpackages.map(({ category }) => category)
      .toSorted()
  ) {
    writer.writeLine(
      `import type * as ${toPascalCase(subpackage)} from "./${subpackage}"`,
    )
  }
  for (const line of PortOneClientInit.split("\n")) {
    writer.writeLine(line)
  }
  writeRootClientObject(srcPath, writer, pack, categoryMap, entityMap)
  const operationPath = path.join(srcPath, "client.ts")
  Deno.writeTextFileSync(operationPath, writer.content + typeWriter.content)
}

const PortOneClientHead = `
/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 */
export function PortOneClient(
  /** 포트원 API Secret */
  secret: string,
  /** 포트원 API를 사용하기 위한 추가 정보 */
  init?: PortOneClientInit,
): PortOneClient {`

function writeRootClientObject(
  srcPath: string,
  writer: Writer,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  for (const line of PortOneClientHead.split("\n")) {
    writer.writeLine(line)
  }
  writer.indent()
  writer.writeLine(`const baseUrl = init?.baseUrl ?? "https://api.portone.io"`)
  writer.writeLine("const storeId = init?.storeId")
  writer.writeLine(`const userAgent = "__USER_AGENT__"`)
  writer.writeLine("return {")
  writer.indent()
  const subpackages = pack.subpackages.filter(({ operations, subpackages }) =>
    operations.length > 0 || subpackages.length > 0
  )
  for (const subpackage of subpackages) {
    writer.writeLine(`${subpackage.category}: {`)
    writer.indent()
    writeClientObject(
      srcPath,
      writer,
      subpackage,
      categoryMap,
      entityMap,
    )
    writer.outdent()
    writer.writeLine("},")
  }
  writer.outdent()
  writer.writeLine("}")
  writer.outdent()
  writer.writeLine("}")
  writer.writeLine("")
  writer.writeLine("export type PortOneClient = {")
  writer.indent()
  for (const subpackage of subpackages) {
    writer.writeLine(
      `${subpackage.category}: ${toPascalCase(subpackage.category)}.Operations`,
    )
  }
  writer.outdent()
  writer.writeLine("}")
}

function writeClientObject(
  parentPath: string,
  implWriter: Writer,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  const currentPath = path.join(parentPath, pack.category)
  const indexPath = path.join(currentPath, "index.ts")
  const typeWriter = Writer()
  const subpackages = pack.subpackages.filter(({ operations, subpackages }) =>
    operations.length > 0 || subpackages.length > 0
  )
  typeWriter.writeLine("")
  typeWriter.writeLine("export type Operations = {")
  typeWriter.indent()
  const crossRef = new Set<string>()
  for (const operation of pack.operations) {
    writeOperation(
      implWriter,
      typeWriter,
      operation,
      categoryMap,
      entityMap,
      crossRef,
    )
  }
  for (const subpackage of subpackages) {
    typeWriter.writeLine(
      `${subpackage.category}: ${toPascalCase(subpackage.category)}.Operations`,
    )
  }
  typeWriter.outdent()
  typeWriter.writeLine("}")
  const sortedRef = [...crossRef]
  sortedRef.sort()
  const imports = sortedRef.map((ref) => {
    const path = categoryMap.get(ref)
    if (!path) {
      throw new Error("unrecognized reference", { cause: { ref } })
    }
    return `import type { ${ref} } from "#generated/${
      path.replace(".", "/")
    }/${ref}"`
  }).concat(
    subpackages.map(({ category }) =>
      `import type * as ${toPascalCase(category)} from "./${category}"`
    ),
  ).join("\n")
  Deno.writeTextFileSync(
    indexPath,
    `${imports}\n${typeWriter.content}`,
    { append: true },
  )
  for (const subpackage of subpackages) {
    implWriter.writeLine(`${subpackage.category}: {`)
    implWriter.indent()
    writeClientObject(
      currentPath,
      implWriter,
      subpackage,
      categoryMap,
      entityMap,
    )
    implWriter.outdent()
    implWriter.writeLine("},")
  }
}

function generateEntityDirectory(
  packagePath: string,
  pack: Package,
  categoryMap: Map<string, string>,
) {
  const indexWriter = Writer()
  for (const entity of pack.entities) {
    const entityPath = path.join(packagePath, `${entity.name}.ts`)
    indexWriter.writeLine(`export type * from "./${entity.name}"`)
    Deno.writeTextFileSync(entityPath, generateEntity(categoryMap, entity))
  }
  for (const subpackage of pack.subpackages) {
    const subPath = path.join(packagePath, subpackage.category)
    fs.ensureDirSync(subPath)
    generateEntityDirectory(subPath, subpackage, categoryMap)
    indexWriter.writeLine(
      `export type * as ${
        toPascalCase(subpackage.category)
      } from "./${subpackage.category}"`,
    )
  }
  const indexPath = path.join(packagePath, "index.ts")
  if (pack.category !== "root") {
    Deno.writeTextFileSync(indexPath, indexWriter.content)
  }
}

function makeCategoryMap(
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

function makeEntityMap(
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
