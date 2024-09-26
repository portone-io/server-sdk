import { z } from "zod"
import { parseDefinition, Property } from "./definition.ts"
import { stripRefPrefix } from "./common.ts"

const SimpleSchema = z.strictObject({
  type: z.string(),
  format: z.string().optional(),
  description: z.string().optional(),
  "x-portone-description": z.string().optional(),
})

const RefSchema = z.strictObject({
  "$ref": z.string(),
})

const ContentSchema = z.strictObject({
  "application/json": z.strictObject({
    schema: SimpleSchema.or(RefSchema),
    example: z.any().optional(),
  }),
}).or(z.strictObject({
  "text/csv": z.strictObject({
    schema: z.strictObject({
      type: z.literal("string"),
      format: z.literal("binary"),
    }),
  }),
}))

const ParameterSchema = z.strictObject({
  name: z.literal("requestBody"),
  in: z.literal("query"),
  required: z.boolean(),
  content: ContentSchema,
}).or(z.strictObject({
  name: z.string(),
  in: z.enum(["path", "query"]),
  description: z.string(),
  required: z.boolean(),
  schema: SimpleSchema.or(RefSchema),
  example: z.any().optional(),
  "x-portone-title": z.string(),
  "x-portone-description": z.string().optional(),
}))

const BodySchema = z.strictObject({
  description: z.string().optional(),
  content: ContentSchema.optional(),
  required: z.boolean().optional(),
  "x-portone-title": z.string().optional(),
  "x-portone-description": z.string().optional(),
})

const SecuritySchema = z.array(
  z.strictObject({
    "bearerJwt": z.array(z.never()),
  }).or(
    z.strictObject({
      "portOne": z.array(z.never()),
    }),
  ),
)

const OperationSchema = z.strictObject({
  summary: z.string().optional(),
  description: z.string().optional(),
  operationId: z.string(),
  requestBody: BodySchema.optional(),
  parameters: z.array(ParameterSchema).optional(),
  responses: z.record(BodySchema),
  security: SecuritySchema.optional(),
  "x-portone-category": z.string().optional(),
  "x-portone-title": z.string().optional(),
  "x-portone-description": z.string().optional(),
  "x-portone-error": RefSchema,
  "x-portone-unstable": z.boolean().optional(),
})

export type Response = {
  type: "application/json"
  schema: string
} | {
  type: "text/csv"
}

export type Operation = {
  id: string
  path: string
  method: string
  params: {
    path: Property[]
    query: Property[]
    body: Property | null
  }
  response: Response | null
  errors: string
  category: string | null
  description: string | null
  unstable: boolean
}

export function parseOperation(
  path: string,
  method: string,
  operationSchema: unknown,
): Operation {
  const { data, success, error } = OperationSchema.safeParse(operationSchema)
  if (!success) {
    throw new Error("failed to parse operationSchema", {
      cause: {
        operationSchema,
        issues: error.issues,
      },
    })
  }
  const content = data.responses["200"].content
  const response = content ? parseResponse(content) : null
  const pathParams = []
  const queryParams = []
  let requestBody = data.requestBody
  for (const parameter of data.parameters ?? []) {
    if ("content" in parameter) {
      requestBody = parameter
    } else if (parameter.in === "path") {
      pathParams.push({
        required: parameter.required ?? false,
        ...parseDefinition(parameter.name, {
          ...parameter.schema,
          description: parameter.description,
        }),
      })
    } else if (parameter.in === "query") {
      queryParams.push({
        required: parameter.required ?? false,
        ...parseDefinition(parameter.name, {
          ...parameter.schema,
          description: parameter.description,
        }),
      })
    }
  }
  let bodyParam = null
  if (requestBody) {
    if (!(requestBody.content && "application/json" in requestBody.content)) {
      throw new Error("unrecognized requestBody format", {
        cause: { operationSchema },
      })
    }
    requestBody.content["application/json"].schema
    bodyParam = {
      required: requestBody.required ?? false,
      ...parseDefinition(
        "requestBody",
        requestBody.content["application/json"].schema,
      ),
    }
  }
  return ({
    id: data.operationId,
    path,
    method,
    params: {
      path: pathParams,
      query: queryParams,
      body: bodyParam,
    },
    response,
    errors: stripRefPrefix(data["x-portone-error"].$ref),
    category: data["x-portone-category"] ?? null,
    description: data.description ?? null,
    unstable: data["x-portone-unstable"] ?? false,
  })
}

function parseResponse(content: z.infer<typeof ContentSchema>): Response {
  for (const [key, value] of Object.entries(content)) {
    switch (key) {
      case "application/json":
        if (!("$ref" in value.schema)) {
          throw new Error("ref not in response content", {
            cause: { content },
          })
        }
        return {
          type: "application/json",
          schema: stripRefPrefix(value.schema.$ref),
        }
      case "text/csv":
        return {
          type: "text/csv",
        }
      default:
        throw new Error("invalid key in response content", {
          cause: { content },
        })
    }
  }
  throw new Error("empty response content", { cause: { content } })
}
