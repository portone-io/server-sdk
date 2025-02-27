import * as fs from "@std/fs"
import * as path from "@std/path"
import { toPascalCase } from "@std/text"
import { makeCategoryMap, makeEntityMap } from "../common/maps.ts"
import {
  entities as webhookEntities,
  types as webhookTypes,
} from "../common/webhook.ts"
import type { Definition, Property } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"
import {
  Extends,
  filterName,
  KotlinWriter,
  toException,
  toPackageCase,
} from "./common.ts"
import { writeDescription } from "./description.ts"
import { generateEntity } from "./entity.ts"
import { writeOperation } from "./operation.ts"
import { generateEntity as generateWebhookEntity } from "./webhook.ts"

export function generateProject(projectRoot: string, pack: Package) {
  const packagePath = path.join(
    projectRoot,
    "lib/src/generated/kotlin/io/portone/sdk/server",
  )
  if (fs.existsSync(packagePath)) {
    Deno.removeSync(packagePath, { recursive: true })
  }
  const categoryMap = makeCategoryMap(pack)
  const entityMap = makeEntityMap(pack)
  const parentsMap = new Map<string, Property[]>()
  const childrenMap = new Map<string, Extends>()
  makeExtendsMap(pack, entityMap, parentsMap, childrenMap)
  const bodies = collectBody(pack)
  const internals = filterUsedAnotherPlace(pack, bodies)
  const oneOfErrors = new Set<string>()
  const variantErrors = new Map<string, Set<string>>()
  collectErrors(pack, entityMap, oneOfErrors, variantErrors)
  const errors = oneOfErrors.union(new Set(variantErrors.keys()))
  const operationCategoryMap = new Map<string, string>(categoryMap)
  for (const error of errors) {
    categoryMap.set(error, "errors")
  }
  generateExceptions(
    packagePath,
    pack,
    oneOfErrors,
    variantErrors,
    entityMap,
    categoryMap,
    operationCategoryMap,
  )
  generateEntityDirectory(
    packagePath,
    "io.portone.sdk.server",
    pack,
    entityMap,
    categoryMap,
    parentsMap,
    childrenMap,
    errors,
    internals,
  )
  generateWebhook(packagePath)
  generateWebhookSerializer(packagePath)
  generateRootClient(packagePath, pack, entityMap, categoryMap)
}

function generateWebhook(
  packagePath: string,
) {
  const webhookPath = path.join(packagePath, "webhook")
  fs.ensureDirSync(webhookPath)
  for (const entity of webhookEntities) {
    const entityPath = path.join(webhookPath, `${entity.name}.kt`)
    Deno.writeTextFileSync(entityPath, generateWebhookEntity(entity))
  }
}

function generateWebhookSerializer(srcPath: string) {
  const writer = KotlinWriter()
  writer.writeLine("package io.portone.sdk.server.webhook")
  const imports = [
    "kotlinx.serialization.DeserializationStrategy",
    "kotlinx.serialization.json.JsonContentPolymorphicSerializer",
    "kotlinx.serialization.json.JsonElement",
    "kotlinx.serialization.json.contentOrNull",
    "kotlinx.serialization.json.jsonObject",
    "kotlinx.serialization.json.jsonPrimitive",
  ]
  for (const item of imports) {
    writer.writeLine(`import ${item}`)
  }
  writer.writeLine("")
  writer.writeLine(
    "internal object WebhookSerializer : JsonContentPolymorphicSerializer<Webhook>(Webhook::class) {",
  )
  writer.indent()
  writer.writeLine(
    `override fun selectDeserializer(element: JsonElement): DeserializationStrategy<Webhook> = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {`,
  )
  writer.indent()
  for (const [value, name] of webhookTypes) {
    writer.writeLine(`"${value}" -> ${name}.serializer()`)
  }
  writer.writeLine("else -> Webhook.Unrecognized.serializer()")
  writer.outdent()
  writer.writeLine("}")
  writer.outdent()
  writer.writeLine("}")
  Deno.writeTextFileSync(
    path.join(srcPath, "webhook", "WebhookSerializer.kt"),
    writer.content,
  )
}

function generateCategoryExceptions(
  errorPath: string,
  pack: Package,
  hierarchy: string,
  parentException?: string,
) {
  if (pack.subpackages.length === 0 && pack.operations.length === 0) return
  const writer = KotlinWriter()
  writer.writeLine("package io.portone.sdk.server.errors")
  writer.writeLine("")
  const name = pack.category === "root"
    ? "RestException"
    : `${hierarchy}Exception`
  const extend = parentException ? ` : ${parentException}` : ""
  writer.writeLine(`public sealed interface ${name}${extend} {`)
  writer.indent()
  writer.writeLine(
    `public${parentException == null ? "" : " override"} val message: String?`,
  )
  writer.outdent()
  writer.writeLine("}")
  for (const subpackage of pack.subpackages) {
    generateCategoryExceptions(
      errorPath,
      subpackage,
      `${hierarchy}${toPascalCase(subpackage.category)}`,
      name,
    )
  }
  Deno.writeTextFileSync(path.join(errorPath, `${name}.kt`), writer.content)
}

function generateExceptions(
  packagePath: string,
  pack: Package,
  oneOfErrors: Set<string>,
  variantErrors: Map<string, Set<string>>,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  operationCategoryMap: Map<string, string>,
) {
  const errorPath = path.join(packagePath, "errors")
  fs.ensureDirSync(errorPath)
  generateCategoryExceptions(errorPath, pack, "")
  {
    const writer = KotlinWriter()
    writer.writeLine("package io.portone.sdk.server.errors")
    writer.writeLine("")
    const extension = [...oneOfErrors].toSorted().map((error) =>
      toException(error)
    ).join(", ")
    writer.writeLine(
      `public class UnknownException internal constructor(public override val message: String) : PortOneException(message), ${extension}`,
    )
    Deno.writeTextFileSync(
      path.join(errorPath, "UnknownException.kt"),
      writer.content,
    )
  }
  for (const error of oneOfErrors) {
    const category = operationCategoryMap.get(error)
    if (!category) continue
    const writer = KotlinWriter()
    writer.writeLine("package io.portone.sdk.server.errors")
    writer.writeLine("")
    writer.writeLine(
      `public sealed interface ${toException(error)} : ${
        toPascalCase(category)
      }Exception {`,
    )
    writer.indent()
    writer.writeLine("public override val message: String?")
    writer.outdent()
    writer.writeLine("}")
    Deno.writeTextFileSync(
      path.join(errorPath, `${toException(error)}.kt`),
      writer.content,
    )
  }
  for (const [error, parents] of variantErrors.entries()) {
    const writer = KotlinWriter()
    const category = categoryMap.get(error)
    if (!category) {
      throw new Error("unrecognized error ref", { cause: { ref: error } })
    }
    const crossRef = new Set([
      "java.lang.Exception",
      `io.portone.sdk.server.${toPackageCase(category)}.${error}`,
    ])
    const definition = entityMap.get(error)
    if (!definition) {
      throw new Error("unrecognized error reference", { cause: { ref: error } })
    }
    if (definition.type !== "object") {
      throw new Error("unsupported error type", { cause: { definition } })
    }
    writer.writeLine("")
    writeDescription(writer, definition.description)
    writer.writeLine(`public class ${toException(error)} internal constructor(`)
    writer.indent()
    writer.writeLine(`cause: ${error}`)
    writer.outdent()
    const extension = [...parents].toSorted().map((parent) =>
      `${toException(parent)}`
    ).join(", ")
    writer.writeLine(`) : PortOneException(cause.message), ${extension} {`)
    writer.indent()
    for (const property of definition.properties) {
      if (property.name === "type" || property.name === "message") continue
      const description = ([] as string[]).concat(property.title ?? [])
        .concat(property.description ?? []).join("\n\n")
      const name = filterName(property.name)
      const wrapOptional = (type: string) =>
        property.required ? type : `${type}?`
      switch (property.type) {
        case "string":
          writeDescription(writer, property.description)
          if (property.format === "date-time") {
            writer.writeLine(
              `public val ${name}: ${
                wrapOptional("Instant")
              } = cause.${property.name}`,
            )
            crossRef.add("java.time.Instant")
            break
          }
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("String")
            } = cause.${property.name}`,
          )
          crossRef.add("kotlin.String")
          break
        case "boolean":
          writeDescription(writer, description)
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("Boolean")
            } = cause.${property.name}`,
          )
          break
        case "number":
          writeDescription(writer, description)
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("Double")
            } = cause.${property.name}`,
          )
          break
        case "integer":
          writeDescription(writer, description)
          if (property.format === "int64") {
            writer.writeLine(
              `public val ${name}: ${
                wrapOptional("Long")
              } = cause.${property.name}`,
            )
            break
          }
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("Int")
            } = cause.${property.name}`,
          )
          break
        case "ref": {
          writeDescription(writer, description)
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional(property.value)
            } = cause.${property.name}`,
          )
          const category = categoryMap.get(property.value)
          if (!category) {
            throw new Error("unrecognized cross reference", {
              cause: { ref: property.value },
            })
          }
          crossRef.add(
            `io.portone.sdk.server.${
              toPackageCase(category)
            }.${property.value}`,
          )
          break
        }
        case "array":
          writeDescription(writer, description)
          switch (property.item.type) {
            case "string":
              crossRef.add("kotlin.Array")
              if (property.item.format === "date-time") {
                writer.writeLine(
                  `public val ${name}: ${
                    wrapOptional("List<Instant>")
                  } = cause.${property.name}`,
                )
                crossRef.add("java.time.Instant")
                break
              }
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("List<String>")
                } = cause.${property.name}`,
              )
              crossRef.add("kotlin.String")
              break
            case "boolean":
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("BooleanArray")
                } = cause.${property.name}`,
              )
              crossRef.add("kotlin.BooleanArray")
              break
            case "number":
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("DoubleArray")
                } = cause.${property.name}`,
              )
              crossRef.add("kotlin.DoubleArray")
              break
            case "integer":
              if (property.item.format === "int64") {
                writer.writeLine(
                  `public val ${name}: ${
                    wrapOptional("LongArray")
                  } = cause.${property.name}`,
                )
                crossRef.add("kotlin.LongArray")
                break
              }
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("IntArray")
                } = cause.${property.name}`,
              )
              crossRef.add("kotlin.IntArray")
              break
            case "ref": {
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional(`List<${property.item.value}>`)
                } = cause.${property.name}`,
              )
              const category = categoryMap.get(property.item.value)
              if (!category) {
                throw new Error("unrecognized cross reference", {
                  cause: { ref: property.item.value },
                })
              }
              crossRef.add(
                `io.portone.sdk.server.${
                  toPackageCase(category)
                }.${property.item.value}`,
              )
              break
            }
            case "discriminant":
            case "object":
            case "oneOf":
            case "enum":
            case "array":
              throw new Error("unsupported array item type", {
                cause: { definition },
              })
            default:
              throw new Error("unrecognized definition type", {
                cause: { definition },
              })
          }
          break
        case "object":
          if (property.properties.length !== 0) {
            throw new Error(
              "properties with their properties specified are not supported",
              { cause: { definition } },
            )
          }
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("JsonObject")
            } = cause.${property.name},`,
          )
          crossRef.add("kotlinx.serialization.json.JsonObject")
          break
        case "discriminant":
        case "enum":
        case "oneOf":
          throw new Error("unsupported property type", {
            cause: { definition },
          })
      }
    }
    writer.outdent()
    writer.writeLine("}")
    const content = [
      "package io.portone.sdk.server.errors",
      [...crossRef].toSorted().map((ref) => `import ${ref}`).join("\n"),
      writer.content,
    ].join("\n\n")
    Deno.writeTextFileSync(
      path.join(errorPath, `${toException(error)}.kt`),
      content,
    )
  }
}

const PortOneClientHeader = `
/**
 * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
 *
 * @param apiSecret 포트원 API Secret입니다.
 * @param apiBase 포트원 REST API 주소입니다. 기본값은 \`"https://api.portone.io"\`입니다.
 * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
 */
public class PortOneClient(
  private val apiSecret: String,
  private val apiBase: String = "https://api.portone.io",
  private val storeId: String? = null,
) : Closeable {
  private val client: HttpClient = HttpClient(OkHttp)

  private val json: Json = Json { ignoreUnknownKeys = true }
`
function generateRootClient(
  packagePath: string,
  pack: Package,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
) {
  const writer = KotlinWriter()
  writer.writeLine("package io.portone.sdk.server")
  writer.writeLine("")
  const crossRef = new Set([
    "io.ktor.client.HttpClient",
    "kotlinx.serialization.json.Json",
    "java.io.Closeable",
    "io.ktor.client.engine.okhttp.OkHttp",
  ])
  const subpackages = pack.subpackages.filter(({ subpackages, operations }) =>
    subpackages.length > 0 || operations.length > 0
  )
  for (const subpackage of subpackages) {
    crossRef.add(
      `io.portone.sdk.server.${toPackageCase(subpackage.category)}.${
        toPascalCase(subpackage.category)
      }Client`,
    )
  }
  for (const ref of [...crossRef].toSorted()) {
    writer.writeLine(`import ${ref}`)
  }
  writer.writeLine("")
  for (const line of PortOneClientHeader.split("\n")) {
    writer.writeLine(line)
  }
  writer.indent()
  for (const subpackage of subpackages) {
    writer.writeLine(
      `public val ${subpackage.category}: ${
        toPascalCase(subpackage.category)
      }Client = ${
        toPascalCase(subpackage.category)
      }Client(apiSecret, apiBase, storeId)`,
    )
    generateClient(
      `io.portone.sdk.server.${toPackageCase(subpackage.category)}`,
      path.join(packagePath, toPackageCase(subpackage.category)),
      subpackage,
      entityMap,
      categoryMap,
    )
  }
  writer.writeLine("override fun close() {")
  writer.indent()
  for (const subpackage of subpackages) {
    writer.writeLine(`${subpackage.category}.close()`)
  }
  writer.writeLine("client.close()")
  writer.outdent()
  writer.writeLine("}")
  writer.outdent()
  writer.writeLine("}")
  const clientPath = path.join(packagePath, "PortOneClient.kt")
  Deno.writeTextFileSync(clientPath, writer.content)
}

function generateClient(
  hierarchy: string,
  packagePath: string,
  pack: Package,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
) {
  const crossRef = new Set([
    "io.ktor.client.HttpClient",
    "kotlinx.serialization.json.Json",
    "java.io.Closeable",
    "io.ktor.client.engine.okhttp.OkHttp",
  ])
  const writer = KotlinWriter()
  writer.writeLine("/**")
  writer.writeLine(" * API Secret을 사용해 포트원 API 클라이언트를 생성합니다.")
  writer.writeLine(" *")
  writer.writeLine(" * @param apiSecret 포트원 API Secret입니다.")
  writer.writeLine(
    ` * @param apiBase 포트원 REST API 주소입니다. 기본값은 \`"https://api.portone.io"\`입니다.`,
  )
  writer.writeLine(
    " * @param storeId 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.",
  )
  writer.writeLine(" */")
  writer.writeLine(
    `public class ${toPascalCase(pack.category)}Client(`,
  )
  writer.indent()
  writer.writeLine("private val apiSecret: String,")
  writer.writeLine(`private val apiBase: String = "https://api.portone.io",`)
  writer.writeLine("private val storeId: String? = null,")
  writer.outdent()
  writer.writeLine("): Closeable {")
  writer.indent()
  writer.writeLine("private val client: HttpClient = HttpClient(OkHttp)")
  writer.writeLine("")
  writer.writeLine("private val json: Json = Json { ignoreUnknownKeys = true }")
  for (const operation of pack.operations) {
    writeOperation(writer, operation, entityMap, categoryMap, crossRef)
  }
  const subpackages = pack.subpackages.filter(({ subpackages, operations }) =>
    subpackages.length > 0 || operations.length > 0
  )
  for (const subpackage of subpackages) {
    writer.writeLine(
      `public val ${subpackage.category}: ${
        toPascalCase(subpackage.category)
      }Client = ${
        toPascalCase(subpackage.category)
      }Client(apiSecret, apiBase, storeId)`,
    )
    crossRef.add(
      `${hierarchy}.${toPackageCase(subpackage.category)}.${
        toPascalCase(subpackage.category)
      }Client`,
    )
    generateClient(
      `${hierarchy}.${toPackageCase(subpackage.category)}`,
      path.join(packagePath, toPackageCase(subpackage.category)),
      subpackage,
      entityMap,
      categoryMap,
    )
  }
  writer.writeLine("override fun close() {")
  writer.indent()
  for (const subpackage of subpackages) {
    writer.writeLine(`${subpackage.category}.close()`)
  }
  writer.writeLine("client.close()")
  writer.outdent()
  writer.writeLine("}")
  writer.outdent()
  writer.writeLine("}")
  const imports = [...crossRef].toSorted().map((ref) => `import ${ref}`).join(
    "\n",
  )
  const content = [`package ${hierarchy}`, imports, writer.content].join("\n\n")
  Deno.writeTextFileSync(
    path.join(packagePath, `${toPascalCase(pack.category)}Client.kt`),
    content,
  )
}

function generateEntityDirectory(
  packagePath: string,
  hierarchy: string,
  pack: Package,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  parentsMap: Map<string, Property[]>,
  childrenMap: Map<string, Extends>,
  errors: Set<string>,
  internals: Set<string>,
) {
  for (const entity of pack.entities) {
    if (errors.has(entity.name)) continue
    const entityPath = path.join(packagePath, `${entity.name}.kt`)
    const visibility = internals.has(entity.name) ? "internal" : "public"
    Deno.writeTextFileSync(
      entityPath,
      generateEntity(
        hierarchy,
        categoryMap,
        parentsMap,
        childrenMap,
        entity,
        visibility,
        visibility,
      ),
    )
  }
  if (pack.category === "root") {
    for (const name of errors) {
      const entity = entityMap.get(name)
      if (!entity) {
        throw new Error("unrecognized error ref", { cause: { ref: name } })
      }
      const entityPath = path.join(packagePath, "errors", `${entity.name}.kt`)
      Deno.writeTextFileSync(
        entityPath,
        generateEntity(
          `${hierarchy}.errors`,
          categoryMap,
          parentsMap,
          childrenMap,
          entity,
          "internal",
          "internal",
        ),
      )
    }
  }
  for (const subpackage of pack.subpackages) {
    const subPath = path.join(packagePath, subpackage.category.toLowerCase())
    fs.ensureDirSync(subPath)
    generateEntityDirectory(
      subPath,
      `${hierarchy}.${subpackage.category.toLowerCase()}`,
      subpackage,
      entityMap,
      categoryMap,
      parentsMap,
      childrenMap,
      errors,
      internals,
    )
  }
}

function collectBody(
  pack: Package,
  internals: Set<string> = new Set(),
) {
  for (const operation of pack.operations) {
    const { body } = operation.params
    if (!body) continue
    if (body.type === "ref") {
      internals.add(body.value)
    }
  }
  for (const subpackage of pack.subpackages) {
    collectBody(subpackage, internals)
  }
  return internals
}

function filterUsedAnotherPlace(
  pack: Package,
  entities: Set<string>,
  filtered: Set<string> = entities,
): Set<string> {
  for (const entity of pack.entities) {
    if (entity.type !== "object") continue
    for (const property of entity.properties) {
      if (property.type === "ref") {
        filtered.delete(property.value)
      } else if (property.type === "array" && property.item.type === "ref") {
        filtered.delete(property.item.value)
      }
    }
  }
  for (const subpackage of pack.subpackages) {
    filterUsedAnotherPlace(subpackage, entities, filtered)
  }
  return filtered
}

function collectErrors(
  pack: Package,
  entityMap: Map<string, Definition>,
  oneOfErrors: Set<string>,
  variantErrors: Map<string, Set<string>>,
) {
  for (const operation of pack.operations) {
    const errorEntity = entityMap.get(operation.errors)
    if (!errorEntity) {
      throw new Error("unrecognized error", { cause: { operation } })
    }
    switch (errorEntity.type) {
      case "object":
        {
          let parents = variantErrors.get(errorEntity.name)
          if (parents == null) {
            parents = new Set()
            variantErrors.set(errorEntity.name, parents)
          }
        }
        break
      case "oneOf":
        oneOfErrors.add(errorEntity.name)
        for (const variant of errorEntity.variants) {
          let parents = variantErrors.get(variant.name)
          if (parents == null) {
            parents = new Set()
            variantErrors.set(variant.name, parents)
          }
          parents.add(errorEntity.name)
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

function makeExtendsMap(
  pack: Package,
  entityMap: Map<string, Definition>,
  parentsMap: Map<string, Property[]>,
  childrenMap: Map<string, Extends>,
) {
  for (const entity of pack.entities) {
    if (entity.type === "oneOf") {
      let recognized: Property[] | null = null
      for (const variant of entity.variants) {
        const variantDefinition = entityMap.get(variant.name)
        if (variantDefinition == null || variantDefinition.type !== "object") {
          throw new Error("unrecognized oneOf variant", {
            cause: { definition: entity },
          })
        }
        if (recognized === null) {
          recognized = [...variantDefinition.properties]
        } else {
          recognized = recognized.flatMap((left) =>
            variantDefinition.properties.filter((right) =>
              left.name === right.name && left.type === right.type &&
              (left.type !== "ref" || right.type !== "ref" ||
                left.value === right.value)
            ).map((right) => ({
              ...right,
              required: left.required && right.required,
            }))
          )
        }
      }
      if (recognized) {
        parentsMap.set(entity.name, recognized)
        for (const variant of entity.variants) {
          let extend = childrenMap.get(variant.name)
          if (extend == null) {
            extend = {
              parents: new Set(),
              properties: new Set(),
            }
            childrenMap.set(variant.name, extend)
          }
          extend.parents.add(entity.name)
          for (const { name } of recognized) {
            extend.properties.add(name)
          }
        }
      }
    }
  }
  for (const subpackage of pack.subpackages) {
    makeExtendsMap(subpackage, entityMap, parentsMap, childrenMap)
  }
}
