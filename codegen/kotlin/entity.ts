import type { Definition } from "../parser/definition.ts"
import {
  filterName,
  KotlinWriter,
  type Override,
  toPackageCase,
} from "./common.ts"
import { writeDescription } from "./description.ts"

export function generateEntity(
  hierarchy: string,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  definition: Definition,
  overridesMap: Map<string, Override>,
  visibility = "public",
  constructorVisibility = "public",
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
      let properties = definition.properties
      if (definition.additionalProperties) {
        const entity = entityMap.get(definition.additionalProperties)
        if (!entity) {
          throw new Error("unrecognized additionalProperties", {
            cause: { ref: properties },
          })
        }
        if (entity.type !== "object") {
          throw new Error("unsupported additionalProperties type", {
            cause: { entity },
          })
        }
        properties = properties.concat(entity.properties)
      }
      const firstProperty = properties[0]
      if (firstProperty?.type === "discriminant") {
        writer.writeLine(`@SerialName("${firstProperty.value}")`)
        crossRef.add("kotlinx.serialization.SerialName")
      }
      const overrides = overridesMap.get(definition.name) ?? {
        properties: new Set(),
        from: new Set(),
      }
      for (const name of overrides.from) {
        const category = categoryMap.get(name)
        if (!category) {
          throw new Error("unrecognized error ref", { cause: { ref: name } })
        }
        crossRef.add(
          `io.portone.sdk.server.${toPackageCase(category)}.${name}`,
        )
      }
      if (visibility !== constructorVisibility) {
        writer.writeLine("@ConsistentCopyVisibility")
        crossRef.add("kotlin.ConsistentCopyVisibility")
      }
      const nonDiscriminant = properties.filter(({ type }) =>
        type !== "discriminant"
      )
      if (nonDiscriminant.length === 0) {
        const extend = [...overrides.from].toSorted()
        const extendList = extend.length > 0 ? extend.join(", ") : null
        writer.writeLine(
          `${visibility} data object ${definition.name}${
            extendList ? `: ${extendList}` : ""
          }`,
        )
        break
      }
      const constructor_ = visibility === constructorVisibility
        ? ""
        : ` ${constructorVisibility} constructor`
      writer.writeLine(
        `${visibility} data class ${definition.name}${constructor_}(`,
      )
      writer.indent()
      const required = nonDiscriminant.filter(({ required }) => required)
      const optional = nonDiscriminant.filter(({ required }) => !required)
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
              writer.writeLine(
                `${val}: @Serializable(InstantSerializer::class) ${
                  wrapOptional("Instant")
                },`,
              )
              crossRef.add(
                "io.portone.sdk.server.serializers.InstantSerializer",
              )
              crossRef.add("java.time.Instant")
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
                  writer.writeLine(`${val}: ${wrapOptional("List<Instant>")},`)
                  crossRef.add("java.time.Instant")
                  break
                }
                writer.writeLine(`${val}: ${wrapOptional("List<String>")},`)
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
                  `${val}: ${wrapOptional(`List<${property.item.value}>`)},`,
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
      const extend = [...overrides.from].toSorted()
      if (extend.length > 0) {
        extend.forEach((name, i) => {
          const leading = i === 0 ? "): " : ""
          const trailing = i === extend.length - 1 ? "" : ","
          writer.writeLine(`${leading}${name}${trailing}`)
          if (i === 0) {
            writer.indent()
          }
        })
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
      const overrides = overridesMap.get(definition.name)
      if (!overrides) {
        throw new Error("unrecognized oneOf definition", {
          cause: { definition },
        })
      }
      const entity = entityMap.get(definition.variants[0].name)
      if (!entity) {
        throw new Error("unrecognized oneOf variant", {
          cause: { ref: definition.variants[0].name },
        })
      }
      if (entity.type !== "object") {
        throw new Error("unsupported oneOf variant type", { cause: { entity } })
      }
      const intersection = entity.properties.filter(({ name }) =>
        overrides.properties.has(name)
      )
      for (const property of intersection) {
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        const name = filterName(property.name)
        const val = `public val ${name}`
        const wrapOpetional = (type: string) =>
          property.required ? type : `${type}?`
        switch (property.type) {
          case "discriminant":
            continue
          case "string":
            writeDescription(writer, description)
            if (property.format === "date-time") {
              writer.writeLine(`${val}: ${wrapOpetional("Instant")}`)
              crossRef.add("java.time.Instant")
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
                    `${val}: ${wrapOpetional("List<Instant>")}`,
                  )
                  crossRef.add("java.time.Instant")
                  break
                }
                writer.writeLine(`${val}: ${wrapOpetional("List<String>")}`)
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
                  `${val}: ${wrapOpetional(`List<${property.item.value}>`)}`,
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
