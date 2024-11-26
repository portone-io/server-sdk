import type { Writer } from "../common/writer.ts"
import type { Definition, Property } from "../parser/definition.ts"
import type { Operation } from "../parser/operation.ts"
import { annotateDescription, writeDescription } from "./description.ts"

export function writeOperation(
  implWriter: Writer,
  typeWriter: Writer,
  errorWriter: Writer,
  operation: Operation,
  entityMap: Map<string, Definition>,
  crossRef: Set<string>,
  baseError: string,
) {
  const errorType = entityMap.get(operation.errors)
  if (!errorType || errorType.type !== "oneOf") {
    throw new Error("unrecognized error ref", {
      cause: { error: operation.errors },
    })
  }
  const variants = `${
    errorType.variants.map(({ name }) => {
      crossRef.add(name)
      return name
    }).join(" | ")
  } | { readonly type: Unrecognized }`
  errorWriter.writeLine(
    `export class ${operation.errors} extends ${baseError} {`,
  )
  errorWriter.indent()
  errorWriter.writeLine(`declare readonly data: ${variants}`)
  errorWriter.writeLine("/** @ignore */")
  errorWriter.writeLine(`constructor(data: ${variants}) {`)
  errorWriter.indent()
  errorWriter.writeLine(`super(data)`)
  errorWriter.writeLine(
    `Object.setPrototypeOf(this, ${operation.errors}.prototype)`,
  )
  errorWriter.writeLine(`this.name = "${operation.errors}"`)
  errorWriter.outdent()
  errorWriter.writeLine("}")
  errorWriter.outdent()
  errorWriter.writeLine("}")
  const requestBody = fetchBodyProperties(operation.params.body, entityMap)
  const params = operation.params.path.concat(operation.params.query).concat(
    requestBody,
  )
  const isStructureOptional = params.every(({ required }) => !required)
  const errorDescription = `@throws {@link ${operation.errors}}`
  const description = ([] as string[]).concat(
    operation.description?.trimEnd() ?? [],
  ).concat(
    errorDescription,
  ).join("\n\n")
  writeDescription(typeWriter, description)
  typeWriter.writeLine(`${operation.id}: (`)
  implWriter.writeLine(`${operation.id}: async (`)
  typeWriter.indent()
  implWriter.indent()
  writeStructuredParameters(
    typeWriter,
    params,
    isStructureOptional,
    true,
    crossRef,
  )
  writeStructuredParameters(
    implWriter,
    params,
    isStructureOptional,
    false,
    crossRef,
  )
  typeWriter.outdent()
  implWriter.outdent()
  switch (operation.response?.type) {
    case "application/json":
      crossRef.add(operation.response.schema)
      implWriter.writeLine(
        `): Promise<${operation.response.schema}> => {`,
      )
      typeWriter.writeLine(
        `) => Promise<${operation.response.schema}>`,
      )
      break
    case "text/csv":
      implWriter.writeLine("): Promise<string> => {")
      typeWriter.writeLine(") => Promise<string>")
      break
    case undefined:
      implWriter.writeLine("): Promise<void> => {")
      typeWriter.writeLine(") => Promise<void>")
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  implWriter.indent()
  if (isStructureOptional) {
    for (const param of params) {
      implWriter.writeLine(`const ${param.name} = options?.${param.name}`)
    }
  } else {
    implWriter.writeLine("const {")
    implWriter.indent()
    for (const param of params) {
      implWriter.writeLine(`${param.name},`)
    }
    implWriter.outdent()
    implWriter.writeLine("} = options")
  }
  let hasQuery = false
  writeRequestBody(implWriter, requestBody)
  switch (operation.method) {
    case "get":
    case "delete":
      hasQuery = writeQuery(
        implWriter,
        operation.params.query.concat(operation.params.body ?? []),
      )
      break
    case "post":
    case "patch":
    case "put":
      hasQuery = writeQuery(implWriter, operation.params.query)
      break
    default:
      throw new Error("unrecognized operation method", { cause: { operation } })
  }
  implWriter.writeLine("const response = await fetch(")
  implWriter.indent()
  implWriter.writeLine(
    `new URL(${makePathInterpolation(operation.path, hasQuery)}, baseUrl),`,
  )
  implWriter.writeLine("{")
  implWriter.indent()
  implWriter.writeLine(`method: "${operation.method.toUpperCase()}",`)
  implWriter.writeLine("headers: {")
  implWriter.indent()
  implWriter.writeLine("Authorization: `PortOne ${secret}`,")
  implWriter.writeLine(`"User-Agent": USER_AGENT,`)
  implWriter.outdent()
  implWriter.writeLine("},")
  switch (operation.method) {
    case "get":
    case "delete":
      break
    case "post":
    case "patch":
    case "put":
      if (operation.params.body) {
        implWriter.writeLine("body: requestBody,")
      }
      break
    default:
      throw new Error("unsupported operation method", { cause: { operation } })
  }
  implWriter.outdent()
  implWriter.writeLine("},")
  implWriter.outdent()
  implWriter.writeLine(")")
  implWriter.writeLine("if (!response.ok) {")
  implWriter.indent()
  implWriter.writeLine(`throw new ${operation.errors}(await response.json())`)
  implWriter.outdent()
  implWriter.writeLine("}")
  switch (operation.response?.type) {
    case "application/json":
      implWriter.writeLine("return response.json()")
      break
    case "text/csv":
      implWriter.writeLine("return response.text()")
      break
    case undefined:
      break
    default:
      throw new Error("unrecognized response type", {
        cause: { response: operation.response },
      })
  }
  implWriter.outdent()
  implWriter.writeLine("},")
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
  writer.writeLine("const requestBody = JSON.stringify({")
  writer.indent()
  for (const property of body) {
    if (property.name === "storeId") {
      writer.writeLine("storeId: storeId ?? init.storeId,")
    } else {
      writer.writeLine(`${property.name},`)
    }
  }
  writer.outdent()
  writer.writeLine("})")
}

/** 실제로 query가 작성되었는지 반환 */
function writeQuery(writer: Writer, query: Property[]): boolean {
  if (query.length === 0) return false
  writer.writeLine("const query = [")
  writer.indent()
  for (const property of query) {
    writer.writeLine(`["${property.name}", ${property.name}],`)
  }
  writer.outdent()
  writer.writeLine("]")
  writer.indent()
  writer.writeLine(
    ".flatMap(([key, value]) => value == null ? [] : `${key}=${encodeURIComponent(value)}`)",
  )
  writer.writeLine(`.join("&")`)
  writer.outdent()
  return true
}

const PATH_PLACEHOLDER = /\{[^\}]+\}/g
function makePathInterpolation(path: string, hasQuery: boolean) {
  const queryInterpolation = "?${query}"
  if (path.match(PATH_PLACEHOLDER)) {
    const interpolation = path.replaceAll(
      PATH_PLACEHOLDER,
      (placeholder) => `\${encodeURIComponent(${placeholder.slice(1, -1)})}`,
    )
    return hasQuery
      ? `\`${interpolation}${queryInterpolation}\``
      : `\`${interpolation}\``
  }
  return hasQuery ? `\`${path}${queryInterpolation}\`` : `"${path}"`
}

function writeStructuredParameters(
  writer: Writer,
  params: Property[],
  optional: boolean,
  withComment: boolean,
  crossRef: Set<string>,
) {
  const name = optional ? "options?" : "options"
  writer.writeLine(`${name}: {`)
  writer.indent()
  writePropertyList(writer, params, withComment, crossRef)
  writer.outdent()
  writer.writeLine("}")
}

function writePropertyList(
  writer: Writer,
  properties: Property[],
  withComment: boolean,
  crossRef: Set<string>,
) {
  for (const property of properties) {
    if (withComment) {
      const description = ([] as string[]).concat(property.title ?? []).concat(
        property.description ?? [],
      ).join("\n\n")
      writeDescription(writer, annotateDescription(description, property))
    }
    const name = property.required ? property.name : `${property.name}?`
    switch (property.type) {
      case "string":
      case "boolean":
        writer.writeLine(`${name}: ${property.type},`)
        break
      case "number":
      case "integer":
        writer.writeLine(`${name}: number,`)
        break
      case "ref":
        crossRef.add(property.value)
        writer.writeLine(
          `${name}: ${property.value},`,
        )
        break
      case "array":
        switch (property.item.type) {
          case "string":
          case "boolean":
            writer.writeLine(`${name}: ${property.item.type}[],`)
            break
          case "number":
          case "integer":
            writer.writeLine(`${name}: number[],`)
            break
          case "ref":
            crossRef.add(property.item.value)
            writer.writeLine(
              `${name}: ${property.item.value}[], `,
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
        writer.writeLine(`${name}: object, `)
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
