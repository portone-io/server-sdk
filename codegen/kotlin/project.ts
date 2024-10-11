import * as fs from "@std/fs"
import * as path from "@std/path"
import { toPascalCase } from "@std/text"
import { makeCategoryMap, makeEntityMap } from "../common/maps.ts"
import { Definition } from "../parser/definition.ts"
import { Package } from "../parser/openapi.ts"
import {
  filterName,
  KotlinWriter,
  makeOverridesMap,
  Override,
  toException,
  toPackageCase,
} from "./common.ts"
import { writeDescription } from "./description.ts"
import { generateEntity } from "./entity.ts"
import { writeOperation } from "./operation.ts"

export function generateProject(projectRoot: string, pack: Package) {
  const packagePath = path.join(
    projectRoot,
    "lib/generated/main/kotlin/io/portone/sdk/server",
  )
  const categoryMap = makeCategoryMap(pack)
  const entityMap = makeEntityMap(pack)
  const overridesMap = makeOverridesMap(pack, entityMap)
  const variantErrors = new Set<string>()
  collectErrors(pack, entityMap, variantErrors)
  generateEntityDirectory(
    packagePath,
    "io.portone.sdk.server",
    pack,
    entityMap,
    categoryMap,
    overridesMap,
  )
  generateRootClient(packagePath, pack, entityMap, categoryMap)
  generateExceptions(
    packagePath,
    [...variantErrors].toSorted(),
    entityMap,
    categoryMap,
  )
}

function generateExceptions(
  packagePath: string,
  errors: string[],
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
) {
  const errorPath = path.join(packagePath, "errors")
  fs.ensureDirSync(errorPath)
  for (const error of errors) {
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
    writer.writeLine(`public class ${toException(error)}(`)
    writer.indent()
    writer.writeLine(`cause: ${error}`)
    writer.outdent()
    writer.writeLine(") : Exception(cause.message) {")
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
              } = cause.${property.name},`,
            )
            crossRef.add("kotlinx.datetime.Instant")
            break
          }
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("String")
            } = cause.${property.name},`,
          )
          crossRef.add("kotlin.String")
          break
        case "boolean":
          writeDescription(writer, description)
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("Boolean")
            } = cause.${property.name},`,
          )
          break
        case "number":
          writeDescription(writer, description)
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("Double")
            } = cause.${property.name},`,
          )
          break
        case "integer":
          writeDescription(writer, description)
          if (property.format === "int64") {
            writer.writeLine(
              `public val ${name}: ${
                wrapOptional("Long")
              } = cause.${property.name},`,
            )
            break
          }
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional("Int")
            } = cause.${property.name},`,
          )
          break
        case "ref": {
          writeDescription(writer, description)
          writer.writeLine(
            `public val ${name}: ${
              wrapOptional(property.value)
            } = cause.${property.name},`,
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
                    wrapOptional("Array<Instant>")
                  } = cause.${property.name},`,
                )
                crossRef.add("kotlinx.datetime.Instant")
                break
              }
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("Array<String>")
                } = cause.${property.name},`,
              )
              crossRef.add("kotlin.String")
              break
            case "boolean":
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("BooleanArray")
                } = cause.${property.name},`,
              )
              crossRef.add("kotlin.BooleanArray")
              break
            case "number":
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("DoubleArray")
                } = cause.${property.name},`,
              )
              crossRef.add("kotlin.DoubleArray")
              break
            case "integer":
              if (property.item.format === "int64") {
                writer.writeLine(
                  `public val ${name}: ${
                    wrapOptional("LongArray")
                  } = cause.${property.name},`,
                )
                crossRef.add("kotlin.LongArray")
                break
              }
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional("IntArray")
                } = cause.${property.name},`,
              )
              crossRef.add("kotlin.IntArray")
              break
            case "ref": {
              writer.writeLine(
                `public val ${name}: ${
                  wrapOptional(`Array<${property.item.value}>`)
                } = cause.${property.name},`,
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
public class PortOneClient(
  private val apiSecret: String,
  private val storeId: String? = null,
  private val apiBase: String = "https://api.portone.io",
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
  ])
  for (const subpackage of pack.subpackages) {
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
  for (const subpackage of pack.subpackages) {
    writer.writeLine(
      `public val ${subpackage.category}: ${
        toPascalCase(subpackage.category)
      }Client = ${
        toPascalCase(subpackage.category)
      }Client(apiSecret, storeId, apiBase)`,
    )
    generateClient(
      "io.portone.sdk.server",
      path.join(packagePath, toPackageCase(subpackage.category)),
      subpackage,
      entityMap,
      categoryMap,
    )
  }
  writer.writeLine("override fun close() {")
  writer.indent()
  for (const subpackage of pack.subpackages) {
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
  ])
  const writer = KotlinWriter()
  writer.writeLine(`public class ${toPascalCase(pack.category)}Client(`)
  writer.indent()
  writer.writeLine("private val apiSecret: String,")
  writer.writeLine("private val storeId: String,")
  writer.writeLine("private val apiBase: String,")
  writer.outdent()
  writer.writeLine(") : Closeable {")
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
      }Client(apiSecret, storeId, apiBase)`,
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
  overridesMap: Map<string, Override>,
) {
  for (const entity of pack.entities) {
    const entityPath = path.join(packagePath, `${entity.name}.kt`)
    Deno.writeTextFileSync(
      entityPath,
      generateEntity(hierarchy, entityMap, categoryMap, entity, overridesMap),
    )
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
      overridesMap,
    )
  }
}

function collectErrors(
  pack: Package,
  entityMap: Map<string, Definition>,
  variantErrors: Set<string>,
) {
  for (const operation of pack.operations) {
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
    collectErrors(subpackage, entityMap, variantErrors)
  }
}
