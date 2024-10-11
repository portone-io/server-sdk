import { Definition } from "../parser/definition.ts"
import { filterName, KotlinWriter, Override, toPackageCase } from "./common.ts"
import { writeDescription } from "./description.ts"

export function generateEntity(
  hierarchy: string,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  definition: Definition,
  overridesMap: Map<string, Override>,
): string {
  const crossRef = new Set<string>()
  const writer = KotlinWriter()
  writeDescription(
    writer,
    definition.description,
  )
  writer.writeLine("@Serializable")
  crossRef.add("kotlinx.serialization.Serializable")
  switch (definition.type) {
    case "object": {
      const firstProperty = definition.properties[0]
      if (firstProperty?.type === "discriminant") {
        writer.writeLine(`@SerialName("${firstProperty.value}")`)
        crossRef.add("kotlinx.serialization.SerialName")
      }
      writer.writeLine(`public data class ${definition.name}(`)
      writer.indent()
      const overrides = overridesMap.get(definition.name) ?? {
        properties: new Set(),
        from: new Set(),
      }
      const required = definition.properties.filter(({ required }) => required)
      const optional = definition.properties.filter(({ required }) => !required)
      for (const property of required.concat(optional)) {
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        const name = filterName(property.name)
        const val = overrides.properties.has(property.name)
          ? `override val ${name}`
          : `val ${name}`
        const wrapOptional = (type: string) =>
          property.required ? type : `${type}? = null`
        switch (property.type) {
          case "discriminant":
            continue
          case "string":
            writeDescription(writer, description)
            if (property.format === "date-time") {
              writer.writeLine(`${val}: ${wrapOptional("Instant")},`)
              crossRef.add("kotlinx.datetime.Instant")
              break
            }
            writer.writeLine(`${val}: ${wrapOptional("String")},`)
            crossRef.add("kotlin.String")
            break
          case "boolean":
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOptional("Boolean")},`)
            break
          case "number":
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOptional("Double")},`)
            break
          case "integer":
            writeDescription(writer, description)
            if (property.format === "int64") {
              writer.writeLine(`${val}: ${wrapOptional("Long")},`)
              break
            }
            writer.writeLine(`${val}: ${wrapOptional("Int")},`)
            break
          case "ref": {
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOptional(property.value)},`)
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
                  writer.writeLine(`${val}: ${wrapOptional("Array<Instant>")},`)
                  crossRef.add("kotlinx.datetime.Instant")
                  break
                }
                writer.writeLine(`${val}: ${wrapOptional("Array<String>")},`)
                crossRef.add("kotlin.String")
                break
              case "boolean":
                writer.writeLine(`${val}: ${wrapOptional("BooleanArray")},`)
                crossRef.add("kotlin.BooleanArray")
                break
              case "number":
                writer.writeLine(`${val}: ${wrapOptional("DoubleArray")},`)
                crossRef.add("kotlin.DoubleArray")
                break
              case "integer":
                if (property.item.format === "int64") {
                  writer.writeLine(`${val}: ${wrapOptional("LongArray")},`)
                  crossRef.add("kotlin.LongArray")
                  break
                }
                writer.writeLine(`${val}: ${wrapOptional("IntArray")},`)
                crossRef.add("kotlin.IntArray")
                break
              case "ref": {
                writer.writeLine(
                  `${val}: ${wrapOptional(`Array<${property.item.value}>`)},`,
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
            writer.writeLine(`${val}: ${wrapOptional("JsonObject")},`)
            crossRef.add("kotlinx.serialization.json.JsonObject")
            break
          case "enum":
          case "oneOf":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
        }
      }
      writer.outdent()
      const extend = [...overrides.from].concat(
        definition.additionalProperties ?? [],
      ).toSorted()
      if (extend.length > 0) {
        const first = true
        for (const name of extend) {
          if (first) {
            writer.writeLine(`): ${name},`)
            writer.indent()
          } else {
            writer.writeLine(`${name},`)
          }
        }
        writer.outdent()
      } else {
        writer.writeLine(")")
      }
      break
    }
    case "oneOf": {
      writer.writeLine(
        `@JsonClassDiscriminator("${definition.variants[0].property}")`,
      )
      crossRef.add("kotlinx.serialization.json.JsonClassDiscriminator")
      writer.writeLine(`public sealed interface ${definition.name} {`)
      writer.indent()
      const intersection = definition.variants.map((variant) => {
        const entity = entityMap.get(variant.name)
        if (entity?.type !== "object") {
          throw new Error("unsupported oneOf variant type", {
            cause: { entity },
          })
        }
        return entity.properties
      }).reduce((a, b) =>
        a.filter(({ name }) => b.some((property) => property.name === name))
      )
      for (const property of intersection) {
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        const name = filterName(property.name)
        const val = `val ${name}`
        const wrapOpetional = (type: string) =>
          property.required ? type : `${type}?`
        switch (property.type) {
          case "discriminant":
            continue
          case "string":
            writeDescription(writer, description)
            if (property.format === "date-time") {
              writer.writeLine(`${val}: ${wrapOpetional("Instant")},`)
              crossRef.add("kotlinx.datetime.Instant")
              break
            }
            writer.writeLine(`${val}: ${wrapOpetional("String")}`)
            crossRef.add("kotlin.String")
            break
          case "boolean":
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOpetional("Boolean")}`)
            break
          case "number":
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOpetional("Double")}`)
            break
          case "integer":
            writeDescription(writer, description)
            if (property.format === "int64") {
              writer.writeLine(`${val}: ${wrapOpetional("Long")}`)
              break
            }
            writer.writeLine(`${val}: ${wrapOpetional("Int")}`)
            break
          case "ref": {
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOpetional(property.value)}`)
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
                    `${val}: ${wrapOpetional("Array<Instant>")},`,
                  )
                  crossRef.add("kotlinx.datetime.Instant")
                  break
                }
                writer.writeLine(`${val}: ${wrapOpetional("Array<String>")}`)
                crossRef.add("kotlin.String")
                break
              case "boolean":
                writer.writeLine(`${val}: ${wrapOpetional("BooleanArray")}`)
                crossRef.add("kotlin.BooleanArray")
                break
              case "number":
                writer.writeLine(`${val}: ${wrapOpetional("DoubleArray")}`)
                crossRef.add("kotlin.DoubleArray")
                break
              case "integer":
                if (property.item.format === "int64") {
                  writer.writeLine(`${val}: ${wrapOpetional("LongArray")}`)
                  crossRef.add("kotlin.LongArray")
                  break
                }
                writer.writeLine(`${val}: ${wrapOpetional("IntArray")}`)
                crossRef.add("kotlin.IntArray")
                break
              case "ref": {
                writer.writeLine(
                  `${val}: ${wrapOpetional(`Array<${property.item.value}>`)}`,
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
            writer.writeLine(`${val}: ${wrapOpetional("JsonObject")}`)
            crossRef.add("kotlinx.serialization.json.JsonObject")
            break
          case "enum":
          case "oneOf":
            throw new Error("unsupported property type", {
              cause: { definition },
            })
        }
      }
      writer.outdent()
      writer.writeLine("}")
      break
    }
    case "enum":
      writer.writeLine(`public enum class ${definition.name} {`)
      writer.indent()
      for (const { value, title, description } of definition.variants) {
        const mergedDescription = [title ?? []].concat([description ?? []])
          .flat().join("\n\n")
        writeDescription(writer, mergedDescription)
        writer.writeLine(`${value},`)
      }
      writer.outdent()
      writer.writeLine("}")
      break
    case "string":
    case "boolean":
    case "number":
    case "integer":
    case "array":
    case "ref":
      throw new Error("unsupported entity type", { cause: { definition } })
    default:
      throw new Error("unrecognized definition type", { cause: { definition } })
  }
  const sortedRef = [...crossRef]
  sortedRef.sort()
  const imports = sortedRef.map((ref) => {
    return `import ${ref}`
  })
  const content = [`package ${toPackageCase(hierarchy)}`].concat(
    imports.length > 0 ? imports.join("\n") : [],
  )
    .concat(writer.content).join("\n\n")
  return content
}
