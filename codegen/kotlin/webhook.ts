import { Definition } from "../common/webhook.ts"
import { filterName, KotlinWriter } from "./common.ts"
import { writeDescription } from "./description.ts"

export function generateEntity(
  definition: Definition,
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
      const extendList = definition.extends.length > 0
        ? ` : ${definition.extends.join(", ")}`
        : ""
      for (const extension of definition.extends) {
        crossRef.add(
          `io.portone.sdk.server.webhook.${extension}`,
        )
      }
      const properties = definition.properties
      const firstProperty = properties[0]
      if (firstProperty?.type === "discriminant") {
        writer.writeLine(`@SerialName("${firstProperty.value}")`)
        crossRef.add("kotlinx.serialization.SerialName")
      }
      const nonDiscriminant = properties.filter(({ type }) =>
        type !== "discriminant"
      )
      let comma = ","
      if (definition.interface) {
        if (definition.interface.discriminant) {
          writer.writeLine(
            `@JsonClassDiscriminator("${definition.interface.discriminant}")`,
          )
          crossRef.add("kotlinx.serialization.json.JsonClassDiscriminator")
        }
        comma = ""
        writer.writeLine(
          `public sealed interface ${definition.name}${extendList} {`,
        )
      } else {
        crossRef.add("kotlin.ConsistentCopyVisibility")
        writer.writeLine("@ConsistentCopyVisibility")
        if (nonDiscriminant.length === 0) {
          writer.writeLine(
            `public data object ${definition.name}${extendList}`,
          )
          break
        } else {
          writer.writeLine(
            `public data class ${definition.name} internal constructor(`,
          )
        }
      }
      writer.indent()
      const required = nonDiscriminant.filter(({ required }) => required)
      const optional = nonDiscriminant.filter(({ required }) => !required)
      for (const property of required.concat(optional)) {
        const description = property.description
        const name = filterName(property.name)
        const visibility = definition.interface ? "public " : ""
        const overrides = property.overrides ? "override " : ""
        const val = `${visibility}${overrides}val ${name}`
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
                }${comma}`,
              )
              crossRef.add(
                "io.portone.sdk.server.serializers.InstantSerializer",
              )
              crossRef.add("java.time.Instant")
              break
            }
            writer.writeLine(`${val}: ${wrapOptional("String")}${comma}`)
            crossRef.add("kotlin.String")
            break
          case "ref": {
            writeDescription(writer, description)
            writer.writeLine(`${val}: ${wrapOptional(property.value)}${comma}`)
            crossRef.add(
              `io.portone.sdk.server.webhook.${property.value}`,
            )
            break
          }
          case "object":
            throw new Error(
              "object properties are not supported",
              { cause: { definition } },
            )
        }
      }
      writer.outdent()
      if (definition.interface) {
        if (definition.interface.open) {
          writer.indent()
          writer.writeLine("@Serializable")
          writer.writeLine(
            `public data object Unrecognized : ${definition.name}`,
          )
          writer.outdent()
        }
        writer.writeLine("}")
      } else {
        writer.writeLine(
          `)${extendList}`,
        )
      }
      break
    }
    case "string":
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
  const content = ["package io.portone.sdk.server.webhook"].concat(
    imports.length > 0 ? imports.join("\n") : [],
  )
    .concat(writer.content).join("\n\n")
  return content
}
