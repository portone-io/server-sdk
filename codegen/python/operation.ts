import { toSnakeCase } from "../common/casing.ts"
import type { Writer } from "../common/writer.ts"
import type {
  Definition,
  OneOfVariant,
  Property,
} from "../parser/definition.ts"
import type { Operation } from "../parser/operation.ts"
import { annotateDescription } from "../python/description.ts"
import { filterName, intoInlineTypeName, PythonWriter } from "./common.ts"
import { writeDescription } from "./description.ts"

export function writeOperation(
  writer: Writer,
  operation: Operation,
  entityMap: Map<string, Definition>,
  crossRef: Set<string>,
  errorRef: Set<string>,
  typing: Set<string>,
  async: boolean,
) {
  const errors = fetchErrors(operation, entityMap)
  const requestBody = fetchBodyProperties(operation.params.body, entityMap)
  const params = operation.params.path.concat(operation.params.query).concat(
    requestBody,
  ).filter(({ name }) => name !== "storeId")
  if (async) {
    writer.writeLine(`async def ${toSnakeCase(operation.id)}_async(`)
  } else {
    writer.writeLine(`def ${toSnakeCase(operation.id)}(`)
  }
  writer.indent()
  writer.writeLine("self,")
  if (params.length > 0) {
    writer.writeLine("*,")
    writePropertyList(writer, params, crossRef, typing)
  }
  writer.outdent()
  switch (operation.response?.type) {
    case "application/json":
      crossRef.add(operation.response.schema)
      writer.writeLine(
        `) -> ${operation.response.schema}:`,
      )
      break
    case "text/csv":
      writer.writeLine(") -> str:")
      break
    case undefined:
      writer.writeLine(") -> None:")
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  writer.indent()
  const paramWriter = PythonWriter()
  if (params.length > 0) {
    paramWriter.writeLine("Args:")
    paramWriter.indent()
    for (const param of params) {
      const lines = ([] as string[]).concat(param.title ?? []).concat(
        param.description === null
          ? []
          : annotateDescription(param.description, param),
      ).join("\n\n").split("\n")
      const optionalMark = param.required ? "" : ", optional"
      paramWriter.writeLine(
        `${filterName(param.name)} (${
          intoInlineTypeName(param)
        }${optionalMark}):`,
      )
      paramWriter.indent()
      for (const line of lines) {
        paramWriter.writeLine(line)
      }
      paramWriter.outdent()
    }
    paramWriter.outdent()
  }
  const errorWriter = PythonWriter()
  errorWriter.writeLine("Raises:")
  errorWriter.indent()
  errorWriter.writeLine(`${operation.errors}: API 호출이 실패한 경우`)
  errorWriter.writeLine(
    "ValueError: 현재 SDK 버전에서 지원하지 않는 API 응답을 받은 경우",
  )
  const description = ([] as string[]).concat(
    operation.description?.trimEnd() ?? [],
  ).concat(
    paramWriter.content.length > 0 ? paramWriter.content : [],
  ).concat(
    errorWriter.content,
  ).join("\n\n")
  writeDescription(writer, description)
  writeRequestBody(writer, requestBody)
  switch (operation.method) {
    case "get":
    case "delete":
      writeQuery(
        writer,
        operation.params.query,
        operation.params.body !== null,
      )
      break
    case "post":
    case "patch":
    case "put":
      writeQuery(writer, operation.params.query, false)
      break
    default:
      throw new Error("unrecognized operation method", { cause: { operation } })
  }
  if (async) {
    writer.writeLine("response = await self._async_client.request(")
  } else {
    writer.writeLine("response = self._sync_client.request(")
  }
  writer.indent()
  writer.writeLine(`"${operation.method.toUpperCase()}",`)
  writer.writeLine(`${makePathInterpolation(operation.path)},`)
  writer.writeLine("params=query,")
  writer.writeLine("headers={")
  writer.indent()
  writer.writeLine(`"Authorization": f"PortOne {self._secret}",`)
  writer.writeLine(`"User-Agent": USER_AGENT,`)
  writer.outdent()
  writer.writeLine("},")
  switch (operation.method) {
    case "get":
    case "delete":
      break
    case "post":
    case "patch":
    case "put":
      if (operation.params.body) {
        writer.writeLine("json=request_body,")
      }
      break
    default:
      throw new Error("unsupported operation method", { cause: { operation } })
  }
  writer.outdent()
  writer.writeLine(")")
  writer.writeLine("if response.status_code != 200:")
  writer.indent()
  writer.writeLine(
    "error_response = response.json()",
  )
  writer.writeLine("error = None")
  for (const variant of errors) {
    writer.writeLine("try:")
    writer.indent()
    writer.writeLine(
      `error = _deserialize_${toSnakeCase(variant.name)}(error_response)`,
    )
    writer.outdent()
    writer.writeLine("except Exception:")
    writer.indent()
    writer.writeLine("pass")
    writer.outdent()
    writer.writeLine("if error is not None:")
    writer.indent()
    errorRef.add(variant.name)
    writer.writeLine(`raise ${variant.name}(error)`)
    writer.outdent()
  }
  errorRef.add("UnknownError")
  writer.writeLine("raise UnknownError(error_response)")
  writer.outdent()
  switch (operation.response?.type) {
    case "application/json":
      writer.writeLine(
        `return _deserialize_${
          toSnakeCase(operation.response.schema)
        }(response.json())`,
      )
      break
    case "text/csv":
      writer.writeLine("return response.text")
      break
    case undefined:
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  writer.outdent()
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

function writeRequestBody(writer: Writer, body: Property[]) {
  if (body.length === 0) return
  writer.writeLine("request_body = {}")
  for (const property of body) {
    const name = property.name === "storeId"
      ? "self._store_id"
      : filterName(property.name)
    if (!property.required) {
      writer.writeLine(`if ${name} is not None:`)
      writer.indent()
    }
    if (property.type === "ref") {
      writer.writeLine(
        `request_body["${property.name}"] = _serialize_${
          toSnakeCase(property.value)
        }(${name})`,
      )
    } else if (property.type === "array" && property.item.type === "ref") {
      writer.writeLine(
        `request_body["${property.name}"] = [_serialize_${
          toSnakeCase(property.item.value)
        }(item) for item in ${name}]`,
      )
    } else {
      writer.writeLine(`request_body["${property.name}"] = ${name}`)
    }
    if (!property.required) {
      writer.outdent()
    }
  }
}

function writeQuery(
  writer: Writer,
  query: Property[],
  withRequestBody: boolean,
) {
  writer.writeLine("query = []")
  for (const property of query) {
    const name = property.name === "storeId"
      ? "self._store_id"
      : filterName(property.name)
    writer.writeLine(`if ${name} is not None:`)
    writer.indent()
    writer.writeLine(`query.append(("${property.name}", ${name}))`)
    writer.outdent()
  }
  if (withRequestBody) {
    writer.writeLine(`query.append(("requestBody", json.dumps(request_body)))`)
  }
}

const PATH_PLACEHOLDER = /\{[^\}]+\}/g
function makePathInterpolation(path: string) {
  const interpolation = path.replaceAll(
    PATH_PLACEHOLDER,
    (placeholder) => `{quote(${toSnakeCase(placeholder)}, safe='')}`,
  )
  return `f"{self._base_url}${interpolation}"`
}

function writePropertyList(
  writer: Writer,
  properties: Property[],
  crossRef: Set<string>,
  typing: Set<string>,
) {
  for (const property of properties) {
    const name = filterName(property.name)
    const toOptional = (type: string): string => {
      if (!property.required) {
        typing.add("Optional")
        return `Optional[${type}] = None`
      }
      return type
    }
    switch (property.type) {
      case "string":
        writer.writeLine(`${name}: ${toOptional("str")},`)
        break
      case "boolean":
        writer.writeLine(`${name}: ${toOptional("bool")},`)
        break
      case "number":
        writer.writeLine(`${name}: ${toOptional("float")},`)
        break
      case "integer":
        writer.writeLine(`${name}: ${toOptional("int")},`)
        break
      case "ref":
        crossRef.add(property.value)
        writer.writeLine(
          `${name}: ${toOptional(property.value)},`,
        )
        break
      case "array":
        switch (property.item.type) {
          case "string":
            writer.writeLine(`${name}: ${toOptional("list[str]")},`)
            break
          case "boolean":
            writer.writeLine(`${name}: ${toOptional("list[bool]")},`)
            break
          case "number":
            writer.writeLine(`${name}: ${toOptional("list[float]")},`)
            break
          case "integer":
            writer.writeLine(`${name}: ${toOptional("list[int]")},`)
            break
          case "ref":
            crossRef.add(property.item.value)
            writer.writeLine(
              `${name}: ${toOptional(`list[${property.item.value}]`)},`,
            )
            break
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
        writer.writeLine(`${name}: ${toOptional("dict")},`)
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
