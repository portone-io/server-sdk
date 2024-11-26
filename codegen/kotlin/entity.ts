import { toPascalCase } from "@std/text"
import type { Definition, Property } from "../parser/definition.ts"
import { Extends, filterName, KotlinWriter, toPackageCase } from "./common.ts"
import { writeDescription } from "./description.ts"

export function generateEntity(
  hierarchy: string,
  entityMap: Map<string, Definition>,
  categoryMap: Map<string, string>,
  parentsMap: Map<string, Property[]>,
  childrenMap: Map<string, Extends>,
  definition: Definition,
  visibility = "public",
  constructorVisibility = "public",
): string {
  const crossRef = new Set<string>()
  const writer = KotlinWriter()
  const serializerWriter = KotlinWriter()
  writeDescription(
    writer,
    definition.description,
  )
  const extension = childrenMap.get(definition.name)
  const extendList = extension
    ? ` : ${
      [...extension.parents].toSorted().map((parent) => `${parent}.Recognized`)
        .join(", ")
    }`
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
      writer.writeLine("@Serializable")
      crossRef.add("kotlinx.serialization.Serializable")
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

      for (const property of nonDiscriminant) {
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        const name = filterName(property.name)
        const overrides = extension?.properties?.has(property.name)
          ? "override "
          : ""
        const val = `${overrides}val ${name}`
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
      serializerWriter.writeLine(
        `private object ${definition.name}Serializer : JsonContentPolymorphicSerializer<${definition.name}>(${definition.name}::class) {`,
      )
      crossRef.add(
        "kotlinx.serialization.json.JsonContentPolymorphicSerializer",
      )
      serializerWriter.indent()
      serializerWriter.writeLine(
        `override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["${definition.property}"]?.jsonPrimitive?.contentOrNull) {`,
      )
      crossRef.add("kotlinx.serialization.json.JsonElement")
      crossRef.add("kotlinx.serialization.json.contentOrNull")
      crossRef.add("kotlinx.serialization.json.jsonObject")
      crossRef.add("kotlinx.serialization.json.jsonPrimitive")
      serializerWriter.indent()
      for (const { value, name } of definition.variants) {
        serializerWriter.writeLine(`"${value}" -> ${name}.serializer()`)
      }
      serializerWriter.writeLine(
        `else -> ${definition.name}.Unrecognized.serializer()`,
      )
      serializerWriter.outdent()
      serializerWriter.writeLine("}")
      serializerWriter.outdent()
      serializerWriter.writeLine("}")
      writer.writeLine(`@Serializable(${definition.name}Serializer::class)`)
      crossRef.add("kotlinx.serialization.Serializable")
      writer.writeLine(`public sealed interface ${definition.name} {`)
      writer.indent()
      writer.writeLine("@Serializable")
      writer.writeLine(
        `@JsonClassDiscriminator("${definition.property}")`,
      )
      crossRef.add("kotlinx.serialization.json.JsonClassDiscriminator")
      writer.writeLine(
        "/** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */",
      )
      writer.writeLine(
        `public sealed interface Recognized : ${definition.name} {`,
      )
      writer.indent()
      const recognized = parentsMap.get(definition.name) ?? []
      for (const property of recognized) {
        const description = ([] as string[]).concat(property.title ?? [])
          .concat(property.description ?? []).join("\n\n")
        const name = filterName(property.name)
        const optional = property.required ? "" : "?"
        switch (property.type) {
          case "discriminant":
            break
          case "string":
            writeDescription(writer, description)
            if (property.format === "date-time") {
              crossRef.add("java.time.Instant")
              writer.writeLine(`public val ${name}: Instant${optional}`)
              break
            }
            crossRef.add("kotlin.String")
            writer.writeLine(`public val ${name}: String${optional}`)
            break
          case "boolean":
            writeDescription(writer, description)
            writer.writeLine(`public val ${name}: Boolean${optional}`)
            break
          case "number":
            writeDescription(writer, description)
            writer.writeLine(`public val ${name}: Double${optional}`)
            break
          case "integer":
            writeDescription(writer, description)
            if (property.format === "int64") {
              writer.writeLine(`public val ${name}: Long${optional}`)
              break
            }
            writer.writeLine(`public val ${name}: Int${optional}`)
            break
          case "ref": {
            writeDescription(writer, description)
            writer.writeLine(`public val ${name}: ${property.value}${optional}`)
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
          case "object":
            writeDescription(writer, description)
            if (property.properties.length !== 0) {
              throw new Error("object with thier properties is not supported", {
                cause: { definition: property },
              })
            }
            crossRef.add("kotlinx.serialization.json.JsonObject")
            writer.writeLine(`public val ${name}: JsonObject${optional}`)
            break
          case "array":
            writeDescription(writer, description)
            switch (property.item.type) {
              case "string":
                crossRef.add("kotlin.Array")
                if (property.item.format === "date-time") {
                  writer.writeLine(
                    `public val ${name}: List<Instant>${optional}`,
                  )
                  crossRef.add("java.time.Instant")
                  break
                }
                writer.writeLine(`public val ${name}: List<String>${optional}`)
                crossRef.add("kotlin.String")
                break
              case "boolean":
                writer.writeLine(`public val ${name}: BooleanArray${optional}`)
                crossRef.add("kotlin.BooleanArray")
                break
              case "number":
                writer.writeLine(`public val ${name}: DoubleArray${optional}`)
                crossRef.add("kotlin.DoubleArray")
                break
              case "integer":
                if (property.item.format === "int64") {
                  writer.writeLine(`public val ${name}: LongArray${optional}`)
                  crossRef.add("kotlin.LongArray")
                  break
                }
                writer.writeLine(`public val ${name}: IntArray${optional}`)
                crossRef.add("kotlin.IntArray")
                break
              case "ref": {
                writer.writeLine(
                  `public val ${name}: List<${property.item.value}>${optional}`,
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
          case "oneOf":
          case "enum":
            throw new Error("unsupported array item type", {
              cause: { definition },
            })
          default:
            throw new Error("unrecognized definition type", {
              cause: { definition },
            })
        }
      }
      writer.outdent()
      writer.writeLine("}")
      writer.writeLine("/** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */")
      writer.writeLine("@Serializable")
      writer.writeLine(`public data object Unrecognized : ${definition.name}`)
      writer.outdent()
      writer.writeLine("}")
      break
    }
    case "enum":
      writer.writeLine(`@Serializable(${definition.name}Serializer::class)`)
      serializerWriter.writeLine(
        `private object ${definition.name}Serializer : KSerializer<${definition.name}> {`,
      )
      crossRef.add("kotlinx.serialization.KSerializer")
      serializerWriter.indent()
      serializerWriter.writeLine(
        `override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(${definition.name}::class.java.name, PrimitiveKind.STRING)`,
      )
      crossRef.add("kotlinx.serialization.descriptors.PrimitiveKind")
      crossRef.add(
        "kotlinx.serialization.descriptors.PrimitiveSerialDescriptor",
      )
      crossRef.add("kotlinx.serialization.descriptors.SerialDescriptor")
      serializerWriter.writeLine(
        `override fun deserialize(decoder: Decoder): ${definition.name} {`,
      )
      crossRef.add("kotlinx.serialization.encoding.Decoder")
      serializerWriter.indent()
      serializerWriter.writeLine("val value = decoder.decodeString()")
      serializerWriter.writeLine("return when (value) {")
      serializerWriter.indent()
      for (const { value } of definition.variants) {
        serializerWriter.writeLine(
          `"${value}" -> ${definition.name}.${toPascalCase(value)}`,
        )
      }
      serializerWriter.writeLine(
        `else -> ${definition.name}.Unrecognized(value)`,
      )
      serializerWriter.outdent()
      serializerWriter.writeLine("}")
      serializerWriter.outdent()
      serializerWriter.writeLine("}")
      serializerWriter.writeLine(
        `override fun serialize(encoder: Encoder, value: ${definition.name}) = encoder.encodeString(value.value)`,
      )
      crossRef.add("kotlinx.serialization.encoding.Encoder")
      serializerWriter.outdent()
      serializerWriter.writeLine("}")
      crossRef.add("kotlinx.serialization.Serializable")
      writer.writeLine(
        `public sealed interface ${definition.name} {`,
      )
      writer.indent()
      writer.writeLine("public val value: String")
      for (const { value, title, description } of definition.variants) {
        const mergedDescription = [title ?? []].concat([description ?? []])
          .flat().join("\n\n")
        writeDescription(writer, mergedDescription)
        writer.writeLine(
          `@Serializable(${toPascalCase(value)}Serializer::class)`,
        )
        writer.writeLine(
          `public data object ${toPascalCase(value)} : ${definition.name} {`,
        )
        writer.indent()
        writer.writeLine(
          `override val value: String = "${value}"`,
        )
        writer.outdent()
        writer.writeLine("}")
        writer.writeLine(
          `private object ${toPascalCase(value)}Serializer : KSerializer<${
            toPascalCase(value)
          }> {`,
        )
        writer.indent()
        writer.writeLine(
          `override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(${
            toPascalCase(value)
          }::class.java.name, PrimitiveKind.STRING)`,
        )
        writer.writeLine(
          `override fun deserialize(decoder: Decoder): ${
            toPascalCase(value)
          } = decoder.decodeString().let {`,
        )
        writer.indent()
        writer.writeLine(`if (it != "${value}") {`)
        writer.indent()
        writer.writeLine(`throw SerializationException(it)`)
        crossRef.add("kotlinx.serialization.SerializationException")
        writer.outdent()
        writer.writeLine("} else {")
        writer.indent()
        writer.writeLine(`return ${toPascalCase(value)}`)
        writer.outdent()
        writer.writeLine("}")
        writer.outdent()
        writer.writeLine("}")
        writer.writeLine(
          `override fun serialize(encoder: Encoder, value: ${
            toPascalCase(value)
          }) = encoder.encodeString(value.value)`,
        )
        writer.outdent()
        writer.writeLine("}")
      }
      writer.writeLine("/** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */")
      writer.writeLine("@ConsistentCopyVisibility")
      writer.writeLine(
        `public data class Unrecognized internal constructor(override val value: String) : ${definition.name}`,
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
    .concat(writer.content).concat(serializerWriter.content).join("\n\n")
  return content
}
