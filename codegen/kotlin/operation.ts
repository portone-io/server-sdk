import type { Writer } from "../common/writer.ts"
import type {
  Definition,
  OneOfVariant,
  Property,
} from "../parser/definition.ts"
import type { Operation } from "../parser/operation.ts"
import {
  filterName,
  KotlinWriter,
  toException,
  toPackageCase,
} from "./common.ts"
import { writeDescription } from "./description.ts"

export function writeOperation(
  writer: Writer,
  operation: Operation,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  crossRef: Set<string>,
) {
  writer.writeLine("")
  let canHaveBody = false
  switch (operation.method) {
    case "get":
      crossRef.add("io.ktor.client.request.`get`")
      canHaveBody = false
      break
    case "delete":
      crossRef.add("io.ktor.client.request.delete")
      canHaveBody = false
      break
    case "post":
      crossRef.add("io.ktor.client.request.post")
      canHaveBody = true
      break
    case "patch":
      crossRef.add("io.ktor.client.request.patch")
      canHaveBody = true
      break
    case "put":
      crossRef.add("io.ktor.client.request.put")
      canHaveBody = true
      break
    default:
      throw new Error("unrecognized operation method", { cause: { operation } })
  }
  const errors = fetchErrors(operation, entityMap)
  for (const { name } of errors) {
    const category = categoryMap.get(name)
    if (!category) {
      throw new Error("unrecognized error ref", { cause: { ref: name } })
    }
    const exception = toException(name)
    crossRef.add(`io.portone.sdk.server.${toPackageCase(category)}.${name}`)
    crossRef.add(`io.portone.sdk.server.errors.${exception}`)
  }
  const requestBody = fetchBodyProperties(operation.params.body, entityMap)
  const params = operation.params.path.concat(operation.params.query).concat(
    requestBody,
  ).filter(({ name }) => name !== "storeId")
  const paramDescription = params.map((property) => {
    const block = ([] as string[]).concat(property.title ?? []).concat(
      property.description ?? [],
    ).join("\n\n")
    return `@param ${property.name}\n${block}`
  }).join("\n")
  const description = ([] as string[]).concat(
    operation.description?.trimEnd() ?? [],
  ).concat(
    paramDescription,
  ).concat(
    `@throws ${toException(operation.errors)}`,
  ).join("\n\n")
  crossRef.add("io.portone.sdk.server.errors.UnknownException")
  writeDescription(writer, description)
  const futureWriter = KotlinWriter()
  writeDescription(futureWriter, "@suppress")
  writer.writeLine(`@JvmName("${operation.id}Suspend")`)
  futureWriter.writeLine(`@JvmName("${operation.id}")`)
  writer.writeLine(`public suspend fun ${operation.id}(`)
  writer.indent()
  writePropertyList(writer, params, crossRef, categoryMap)
  writer.outdent()
  futureWriter.writeLine(`public fun ${operation.id}Future(`)
  futureWriter.indent()
  writePropertyList(futureWriter, params, crossRef, categoryMap)
  futureWriter.outdent()
  const paramList = params.map(({ name }) => name).join(", ")
  switch (operation.response?.type) {
    case "application/json": {
      const category = categoryMap.get(operation.response.schema)
      if (!category) {
        throw new Error("unrecognized cross reference", {
          cause: { ref: operation.response.schema },
        })
      }
      crossRef.add(
        `io.portone.sdk.server.${
          toPackageCase(category)
        }.${operation.response.schema}`,
      )
      writer.writeLine(
        `): ${operation.response.schema} {`,
      )
      futureWriter.writeLine(
        `): CompletableFuture<${operation.response.schema}> = GlobalScope.future { ${operation.id}(${paramList}) }`,
      )
      crossRef.add("java.util.concurrent.CompletableFuture")
      crossRef.add("kotlinx.coroutines.GlobalScope")
      crossRef.add("kotlinx.coroutines.future.future")
      break
    }
    case "text/csv":
      crossRef.add("kotlin.String")
      writer.writeLine("): String {")
      futureWriter.writeLine(
        `): CompletableFuture<String> = GlobalScope.future { ${operation.id}(${paramList}) }`,
      )
      crossRef.add("kotlinx.coroutines.GlobalScope")
      crossRef.add("kotlinx.coroutines.future.future")
      break
    case undefined:
      writer.writeLine(") {")
      futureWriter.writeLine(
        `): CompletableFuture<Unit> = GlobalScope.future { ${operation.id}(${paramList}) }`,
      )
      crossRef.add("kotlinx.coroutines.GlobalScope")
      crossRef.add("kotlinx.coroutines.future.future")
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  writer.indent()
  if (operation.params.body) {
    if (operation.params.body.type !== "ref") {
      throw new Error("unsupported request body type", {
        cause: { definition: operation.params.body },
      })
    }
    const category = categoryMap.get(operation.params.body.value)
    if (!category) {
      throw new Error("unrecognized request body ref", {
        cause: { ref: operation.params.body.value },
      })
    }
    crossRef.add(
      `io.portone.sdk.server.${
        toPackageCase(category)
      }.${operation.params.body.value}`,
    )
    writer.writeLine(`val requestBody = ${operation.params.body.value}(`)
    writer.indent()
    for (const property of requestBody) {
      writer.writeLine(`${property.name} = ${property.name},`)
    }
    writer.outdent()
    writer.writeLine(")")
  }
  writer.writeLine(`val httpResponse = client.${operation.method}(apiBase) {`)
  writer.indent()
  writer.writeLine("url {")
  writer.indent()
  const path = operation.path.split("/").slice(1).map((segment) =>
    segment.startsWith("{") && segment.endsWith("}")
      ? `${segment.slice(1, -1)}.toString()`
      : `"${segment}"`
  ).join(", ")
  crossRef.add("io.ktor.http.appendPathSegments")
  writer.writeLine(`appendPathSegments(${path})`)
  for (const property of operation.params.query) {
    if (property.required) {
      writer.writeLine(
        `parameters.append("${property.name}", ${property.name}.toString())`,
      )
    } else {
      writer.writeLine(
        `if (${property.name} != null) parameters.append("${property.name}", ${property.name}.toString())`,
      )
    }
  }
  if (operation.params.body && !canHaveBody) {
    crossRef.add("kotlinx.serialization.encodeToString")
    writer.writeLine(
      `parameters.append("requestBody", json.encodeToString(requestBody))`,
    )
  }
  writer.outdent()
  writer.writeLine("}")
  crossRef.add("io.ktor.client.request.headers")
  writer.writeLine("headers {")
  writer.indent()
  crossRef.add("io.ktor.http.HttpHeaders")
  writer.writeLine(`append(HttpHeaders.Authorization, "PortOne $apiSecret")`)
  writer.outdent()
  writer.writeLine("}")
  if (canHaveBody && operation.params.body) {
    crossRef.add("io.ktor.http.contentType")
    crossRef.add("io.ktor.http.ContentType")
    writer.writeLine("contentType(ContentType.Application.Json)")
  }
  switch (operation.response?.type) {
    case "application/json":
      crossRef.add("io.ktor.client.request.accept")
      crossRef.add("io.ktor.http.ContentType")
      writer.writeLine("accept(ContentType.Application.Json)")
      break
    case "text/csv":
      crossRef.add("io.ktor.client.request.accept")
      crossRef.add("io.ktor.http.ContentType")
      writer.writeLine("accept(ContentType.Text.CSV)")
      break
    case undefined:
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  crossRef.add("io.ktor.http.userAgent")
  crossRef.add("io.portone.sdk.server.USER_AGENT")
  writer.writeLine("userAgent(USER_AGENT)")
  if (operation.params.body && canHaveBody) {
    crossRef.add("io.ktor.client.request.setBody")
    crossRef.add("kotlinx.serialization.encodeToString")
    writer.writeLine("setBody(json.encodeToString(requestBody))")
  }
  writer.outdent()
  writer.writeLine("}")
  writer.writeLine("if (httpResponse.status.value !in 200..299) {")
  writer.indent()
  crossRef.add("io.ktor.client.call.body")
  writer.writeLine("val httpBody = httpResponse.body<String>()")
  writer.writeLine("val httpBodyDecoded = try {")
  writer.indent()
  {
    const category = categoryMap.get(operation.errors)
    if (!category) {
      throw new Error("unrecognized error ref", {
        cause: { ref: operation.errors },
      })
    }
    crossRef.add(
      `io.portone.sdk.server.${toPackageCase(category)}.${operation.errors}`,
    )
  }
  writer.writeLine(`json.decodeFromString<${operation.errors}>(httpBody)`)
  writer.outdent()
  writer.writeLine("}")
  writer.writeLine("catch (_: Exception) {")
  writer.indent()
  writer.writeLine(`throw UnknownException("Unknown API error: $httpBody")`)
  writer.outdent()
  writer.writeLine("}")
  writer.writeLine("when (httpBodyDecoded) {")
  writer.indent()
  for (const error of errors) {
    writer.writeLine(
      `is ${error.name} -> throw ${toException(error.name)}(httpBodyDecoded)`,
    )
  }
  writer.writeLine(
    `else -> throw UnknownException("Unknown API error: $httpBody")`,
  )
  writer.outdent()
  writer.writeLine("}")
  writer.outdent()
  writer.writeLine("}")
  switch (operation.response?.type) {
    case "application/json":
      writer.writeLine("val httpBody = httpResponse.body<String>()")
      writer.writeLine("return try {")
      writer.indent()
      writer.writeLine(
        `json.decodeFromString<${operation.response.schema}>(httpBody)`,
      )
      writer.outdent()
      writer.writeLine("}")
      writer.writeLine("catch (_: Exception) {")
      writer.indent()
      writer.writeLine(
        `throw UnknownException("Unknown API response: $httpBody")`,
      )
      writer.outdent()
      writer.writeLine("}")
      break
    case "text/csv":
      writer.writeLine("return httpResponse.body<String>()")
      break
    case undefined:
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  writer.outdent()
  writer.writeLine("}")
  writer.writeLine("")
  for (const line of futureWriter.content.split("\n")) {
    writer.writeLine(line)
  }
}

function fetchErrors(
  operation: Operation,
  entityMap: Map<string, Definition>,
): OneOfVariant[] {
  const actualError = entityMap.get(operation.errors)
  if (!actualError) {
    throw new Error("unqualifed error type", { cause: { operation } })
  }
  switch (actualError.type) {
    case "oneOf":
      return actualError.variants
    case "string":
    case "number":
    case "boolean":
    case "object":
    case "ref":
    case "discriminant":
    case "enum":
    case "array":
    case "integer":
      throw new Error("unsupported error type", {
        cause: { error: actualError },
      })
    default:
      throw new Error("unrecognized error type", {
        cause: { error: actualError },
      })
  }
}

function fetchBodyProperties(
  body: Property | null,
  entityMap: Map<string, Definition>,
): Property[] {
  if (!body) return []
  if (body.type !== "ref") {
    throw new Error("unsupported body type", { cause: { body } })
  }
  const actualBody = entityMap.get(body.value)
  if (!actualBody) {
    throw new Error("unrecognized actual body type", { cause: { body } })
  }
  if (actualBody.type !== "object") {
    throw new Error("unsupported actual body type", { cause: { body } })
  }
  const properties = actualBody.properties
  return properties
}

function writePropertyList(
  writer: Writer,
  properties: Property[],
  crossRef: Set<string>,
  categoryMap: Map<string, string>,
) {
  for (const property of properties) {
    const name = filterName(property.name)
    const wrapOptional = (type: string) =>
      property.required ? type : `${type}? = null`
    switch (property.type) {
      case "string":
        if (property.format === "date-time") {
          writer.writeLine(`${name}: ${wrapOptional("Instant")},`)
          crossRef.add("java.time.Instant")
          break
        }
        writer.writeLine(`${name}: ${wrapOptional("String")},`)
        crossRef.add("kotlin.String")
        break
      case "boolean":
        writer.writeLine(`${name}: ${wrapOptional("Boolean")},`)
        break
      case "number":
        writer.writeLine(`${name}: ${wrapOptional("Double")},`)
        break
      case "integer":
        if (property.format === "int64") {
          writer.writeLine(`${name}: ${wrapOptional("Long")},`)
          break
        }
        writer.writeLine(`${name}: ${wrapOptional("Int")},`)
        break
      case "ref": {
        const category = categoryMap.get(property.value)
        if (!category) {
          throw new Error("unrecognized cross reference", {
            cause: { ref: property.value },
          })
        }
        crossRef.add(
          `io.portone.sdk.server.${toPackageCase(category)}.${property.value}`,
        )
        writer.writeLine(
          `${name}: ${wrapOptional(property.value)},`,
        )
        break
      }
      case "array":
        switch (property.item.type) {
          case "string":
            crossRef.add("kotlin.Array")
            if (property.item.format === "date-time") {
              writer.writeLine(`${name}: ${wrapOptional("List<Instant>")},`)
              crossRef.add("java.time.Instant")
              break
            }
            writer.writeLine(`${name}: ${wrapOptional("List<String>")},`)
            crossRef.add("kotlin.String")
            break
          case "boolean":
            writer.writeLine(`${name}: ${wrapOptional("BooleanArray")},`)
            crossRef.add("kotlin.BooleanArray")
            break
          case "number":
            writer.writeLine(`${name}: ${wrapOptional("DoubleArray")},`)
            crossRef.add("kotlin.DoubleArray")
            break
          case "integer":
            if (property.item.format === "int64") {
              writer.writeLine(`${name}: ${wrapOptional("LongArray")},`)
              crossRef.add("kotlin.LongArray")
              break
            }
            writer.writeLine(`${name}: ${wrapOptional("IntArray")},`)
            crossRef.add("kotlin.IntArray")
            break
          case "ref": {
            writer.writeLine(
              `${name}: ${wrapOptional(`List<${property.item.value}>`)},`,
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
          case "object":
          case "oneOf":
          case "discriminant":
          case "enum":
            throw new Error("unsupported array item type", {
              cause: { property },
            })
          default:
            throw new Error("unrecognized property type", {
              cause: { property },
            })
        }
        break
      case "object":
        if (property.properties.length !== 0) {
          throw new Error("unsupported parameter property object type", {
            cause: { property },
          })
        }
        writer.writeLine(`${name}: ${wrapOptional("JsonObject")},`)
        crossRef.add("kotlinx.serialization.json.JsonObject")
        break
      case "oneOf":
      case "discriminant":
      case "enum":
        throw new Error("unsupported parameter property type", {
          cause: { property },
        })
      default:
        throw new Error("unrecognized property type", { cause: { property } })
    }
  }
}
