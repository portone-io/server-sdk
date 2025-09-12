import { z } from "zod"
import { stripRefPrefix } from "./common.ts"

const BaseDefinitionSchema = z.strictObject({
  title: z.string().optional(),
  description: z.string().optional(),
  "x-portone-title": z.string().optional(),
  "x-portone-description": z.string().optional(),
  "x-portone-status-code": z.number().optional(),
})

const RefSchema = BaseDefinitionSchema.extend({
  "$ref": z.string(),
}).strict()

const OneOfSchema = BaseDefinitionSchema.extend({
  oneOf: z.array(RefSchema),
  discriminator: z.strictObject({
    propertyName: z.string(),
    mapping: z.record(z.string()),
  }),
  "x-portone-discriminator": z.record(z.strictObject({
    title: z.string().optional(),
  })).optional(),
}).strict()

const BaseObjectSchema = BaseDefinitionSchema.extend({
  type: z.literal("object"),
  required: z.array(z.string()).optional(),
}).strict()

type ObjectSchema = z.infer<typeof BaseObjectSchema> & {
  properties?: Record<
    string,
    z.infer<typeof DefinitionSchema>
  >
  additionalProperties?: z.infer<typeof DefinitionSchema>
}

const ObjectSchema: z.ZodType<ObjectSchema> = BaseObjectSchema.extend({
  properties: z.lazy(() => z.record(DefinitionSchema)).optional(),
  additionalProperties: z.lazy(() => DefinitionSchema).optional(),
}).strict()

const StringSchema = BaseDefinitionSchema.extend({
  type: z.literal("string"),
  format: z.string().optional(),
}).strict()

const EnumSchema = BaseDefinitionSchema.extend({
  type: z.literal("string"),
  enum: z.array(z.string()),
  "x-portone-enum": z.record(z.strictObject({
    title: z.string().optional(),
    description: z.string().optional(),
  })),
}).strict()

const BaseArraySchema = BaseDefinitionSchema.extend({
  type: z.literal("array"),
  properties: z.any().optional(),
  "x-portone-enum": z.record(z.strictObject({
    title: z.string().optional(),
    description: z.string().optional(),
  })).optional().describe("when item is enum"),
}).strict()

type ArraySchema = z.infer<typeof BaseArraySchema> & {
  items: z.infer<typeof DefinitionSchema>
}

const ArraySchema: z.ZodType<ArraySchema> = BaseArraySchema.extend({
  items: z.lazy(() => DefinitionSchema),
}).strict()

const IntegerSchema = BaseDefinitionSchema.extend({
  type: z.literal("integer"),
  format: z.string().optional(),
}).strict()

const NumberSchema = BaseDefinitionSchema.extend({
  type: z.literal("number"),
  format: z.string().optional(),
}).strict()

const BooleanSchema = BaseDefinitionSchema.extend({
  type: z.literal("boolean"),
}).strict()

const DefinitionSchema = RefSchema.or(OneOfSchema).or(StringSchema).or(
  EnumSchema,
).or(IntegerSchema).or(NumberSchema).or(BooleanSchema).or(
  z.lazy(() => ObjectSchema),
).or(
  z.lazy(() => ArraySchema),
)

export type OneOfVariant = {
  name: string
  value: string
  title: string | null
}

export type OneOfDefinition = {
  type: "oneOf"
  property: string
  variants: OneOfVariant[]
}

export type Property = {
  required: boolean
} & Definition

export type ObjectDefinition = {
  type: "object"
  properties: Property[]
  additionalProperties: Definition | null
}

export type StringDefinition = {
  type: "string"
  format: string | null
}

export type DiscriminantDefinition = {
  type: "discriminant"
  value: string
}

export type EnumDefinition = {
  type: "enum"
  variants: {
    value: string
    title: string | null
    description: string | null
  }[]
}

export type ArrayDefinition = {
  type: "array"
  item: Definition
}

export type RefDefinition = {
  type: "ref"
  value: string
}

export type IntegerDefinition = {
  type: "integer"
  format: string | null
}

export type NumberDefinition = {
  type: "number"
  format: string | null
}

export type BooleanDefinition = {
  type: "boolean"
}

export type Definition =
  & {
    name: string
    title: string | null
    description: string | null
  }
  & (
    | RefDefinition
    | OneOfDefinition
    | ObjectDefinition
    | StringDefinition
    | DiscriminantDefinition
    | EnumDefinition
    | ArrayDefinition
    | IntegerDefinition
    | NumberDefinition
    | BooleanDefinition
  )

export function parseDefinition(name: string, definition: unknown): Definition {
  const { data, success, error } = DefinitionSchema.safeParse(definition)
  if (!success) {
    throw new Error("failed to parse definition", {
      cause: {
        definition,
        issues: error.issues,
      },
    })
  }
  const title = data.title ?? null
  const description = data.description ?? null
  if ("$ref" in data) {
    return {
      name: name,
      title,
      description,
      type: "ref",
      value: stripRefPrefix(data.$ref),
    }
  }
  if ("oneOf" in data) {
    const { propertyName, mapping } = data.discriminator
    const variants = Object.entries(mapping).map(([discriminator, ref]) => ({
      name: stripRefPrefix(ref),
      value: discriminator,
      title: data["x-portone-discriminator"]?.[discriminator]?.title ?? null,
    }))
    return {
      name,
      title,
      description,
      type: "oneOf",
      property: propertyName,
      variants,
    }
  }
  if (data.type === "object") {
    const required = new Set(data.required ?? [])
    const properties = Object.entries(data.properties ?? []).map((
      [name, definition],
    ) => ({
      required: required.has(name),
      ...parseDefinition(name, definition),
    }))
    const additionalProperties = data.additionalProperties === undefined
      ? null
      : parseDefinition("additionalProperties", data.additionalProperties)
    return {
      name,
      title,
      description,
      type: "object",
      properties,
      additionalProperties,
    }
  }
  if (data.type === "string") {
    if ("enum" in data) {
      const portoneEnum = data["x-portone-enum"]
      const variants = data.enum.map((value) => ({
        value,
        title: portoneEnum[value].title ?? null,
        description: portoneEnum[value].description ?? null,
      }))
      return {
        name,
        title,
        description,
        type: "enum",
        variants,
      }
    }
    return {
      name,
      title,
      description,
      type: "string",
      format: data.format ?? null,
    }
  }
  if (data.type === "array") {
    return {
      name,
      title,
      description,
      type: "array",
      item: parseDefinition(name, data.items),
    }
  }
  if (data.type === "integer") {
    return {
      name,
      title,
      description,
      type: "integer",
      format: data.format ?? null,
    }
  }
  if (data.type === "number") {
    return {
      name,
      title,
      description,
      type: "number",
      format: data.format ?? null,
    }
  }
  if (data.type === "boolean") {
    return {
      name,
      title,
      description,
      type: "boolean",
    }
  }
  throw new Error("unrecognized definition type", { cause: { definition } })
}
