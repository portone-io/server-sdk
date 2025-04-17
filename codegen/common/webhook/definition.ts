export type Definition =
  & {
    name: string
    description: string | null
  }
  & (
    | DiscriminantDefinition
    | StringDefinition
    | ObjectDefinition
    | RefDefinition
    | IntegerDefinition
  )

export type Property = {
  required: boolean
  overrides: boolean
} & Definition

type DiscriminantDefinition = {
  type: "discriminant"
  value: string
}

type StringDefinition = {
  type: "string"
  format: string | null
}

type IntegerDefinition = {
  type: "integer"
}

type ObjectDefinition = {
  type: "object"
  extends: string[]
  properties: Property[]
  interface: ObjectInterface | null
}

type ObjectInterface = {
  discriminant: string | null
  coproduct: string[]
  open: boolean
}

type RefDefinition = {
  type: "ref"
  value: string
}

export function extractDiscriminant(
  definition: Definition,
): [string, string][] {
  if (definition.type === "object") {
    for (const property of definition.properties) {
      if (property.type === "discriminant") {
        return [[property.value, definition.name]]
      }
    }
  }
  return []
}

export function extendType(
  self: Omit<Definition & ObjectDefinition, "extends">,
  parent: Definition & ObjectDefinition,
): Definition & ObjectDefinition {
  return {
    ...self,
    properties: self.properties.filter(({ type }) => type === "discriminant")
      .concat(
        parent.properties.filter(({ name }) =>
          self.properties.every(({ name: selfName }) => selfName !== name)
        ).map((property) => ({
          ...property,
          overrides: true,
        })),
      ).concat(self.properties.filter(({ type }) => type !== "discriminant")),
    extends: [parent.name],
  }
}
