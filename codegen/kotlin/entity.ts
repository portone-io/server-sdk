import { toPascalCase } from "@std/text"
import type { Definition } from "../parser/definition.ts"
import { filterName, KotlinWriter, toPackageCase } from "./common.ts"
import { writeDescription } from "./description.ts"

export function generateEntity(
  hierarchy: string,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  extendsMap: Map<string, Set<string>>,
  definition: Definition,
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
  const extension = extendsMap.get(definition.name)
  const extendList = extension
    ? ` : ${[...extension].toSorted().join(", ")}`
    : ""
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
      if (visibility !== constructorVisibility) {
        writer.writeLine("@ConsistentCopyVisibility")
        crossRef.add("kotlin.ConsistentCopyVisibility")
      }
      const nonDiscriminant = properties.filter(({ type }) =>
        type !== "discriminant"
      )
      if (nonDiscriminant.length === 0) {
        writer.writeLine(
          `${visibility} data object ${definition.name}${extendList}`,
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
        const val = `val ${name}`
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
      writer.writeLine(`)${extendList}`)
      break
    }
    case "oneOf": {
      writer.writeLine(
        `@JsonClassDiscriminator("${definition.property}")`,
      )
      crossRef.add("kotlinx.serialization.json.JsonClassDiscriminator")
      writer.writeLine(`public sealed interface ${definition.name} {`)
      writer.indent()
      writer.writeLine(`public data object Unrecognized : ${definition.name}`)
      writer.outdent()
      writer.writeLine("}")
      break
    }
    case "enum":
      writer.writeLine(
        `public sealed class ${definition.name} {`,
      )
      writer.indent()
      for (const { value, title, description } of definition.variants) {
        const mergedDescription = [title ?? []].concat([description ?? []])
          .flat().join("\n\n")
        writeDescription(writer, mergedDescription)
        writer.writeLine(`@SerialName("${value}")`)
        crossRef.add("kotlinx.serialization.SerialName")
        writer.writeLine(
          `public data object ${toPascalCase(value)} : ${definition.name}()`,
        )
      }
      writer.writeLine("@ConsistentCopyVisibility")
      writer.writeLine(
        `public data class Unrecognized internal constructor(public val value: String) : ${definition.name}()`,
      )
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
