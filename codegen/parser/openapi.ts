import OpenAPI from "../openapi.json" with { type: "json" }
import { type Definition, parseDefinition } from "./definition.ts"
import { type Operation, parseOperation } from "./operation.ts"

type DefinitionUsage = {
  definition: Definition
  categories: Set<string | null>
}

export type Package = {
  category: string
  operations: Operation[]
  entities: Definition[]
  subpackages: Package[]
}

function normalizeCategory(category: string | null): string {
  const nonNull = category ?? "platform"
  return nonNull
}

export function packageSchema(): Package {
  const definitionUsages = new Map<string, DefinitionUsage>()
  const shakeDefinition = (category: string | null, definition: Definition) => {
    switch (definition.type) {
      case "ref": {
        const usage = definitionUsages.get(definition.value)
        if (!usage) {
          throw new Error(
            `type ${definition.value} was referenced but not found`,
            { cause: { definition } },
          )
        }
        usage.categories.add(category)
        shakeDefinition(category, usage.definition)
        break
      }
      case "object": {
        for (const property of definition.properties) {
          shakeDefinition(category, property)
        }
        if (definition.additionalProperties) {
          const usage = definitionUsages.get(definition.additionalProperties)
          if (!usage) {
            throw new Error(
              `type ${definition.additionalProperties} was referenced by additionalProperties but not found`,
              { cause: { definition } },
            )
          }
          usage.categories.add(category)
          shakeDefinition(category, usage.definition)
        }
        break
      }
      case "array": {
        shakeDefinition(category, definition.item)
        break
      }
      case "oneOf": {
        for (const { name } of definition.variants) {
          const usage = definitionUsages.get(name)
          if (!usage) {
            throw new Error(`type ${name} was referenced but not found`, {
              cause: { definition },
            })
          }
          usage.categories.add(category)
          shakeDefinition(category, usage.definition)
        }
        break
      }
      case "string":
      case "number":
      case "boolean":
      case "integer":
      case "enum":
      case "discriminant":
        break
      default:
        throw new Error("unrecognized definition type", {
          cause: { definition },
        })
    }
  }

  for (const [name, definition] of Object.entries(OpenAPI.components.schemas)) {
    definitionUsages.set(name, {
      definition: parseDefinition(name, definition),
      categories: new Set(),
    })
  }

  const shakeOperation = (
    operation: Operation,
  ) => {
    const { category, params, response, errors } = operation
    for (const property of params.path) {
      shakeDefinition(category, property)
    }
    for (const property of params.query) {
      shakeDefinition(category, property)
    }
    if (params.body) {
      shakeDefinition(category, params.body)
    }
    if (response?.type === "application/json") {
      const usage = definitionUsages.get(response.schema)
      if (!usage) {
        throw new Error(
          `type ${response.schema} was referenced by response but not found`,
          { cause: { operation } },
        )
      }
      usage.categories.add(category)
      shakeDefinition(category, usage.definition)
    }
    if (errors) {
      const usage = definitionUsages.get(errors)
      if (!usage) {
        throw new Error(`type ${name} was referenced by errors not found`, {
          cause: { operation },
        })
      }
      usage.categories.add(category)
      shakeDefinition(category, usage.definition)
    }
  }
  for (const { definition } of definitionUsages.values()) {
    if (definition.type === "oneOf") {
      for (const { name, property, value } of definition.variants) {
        const usage = definitionUsages.get(name)
        if (!usage) {
          throw new Error(`type ${name} was referenced but not found`, {
            cause: { definition },
          })
        }
        if (usage.definition.type !== "object") {
          throw new Error(
            `type ${usage.definition.name} is oneOf variant but not an object`,
            { cause: { definition: usage.definition } },
          )
        }
        const discriminant = usage.definition.properties.find(({ name }) =>
          name === property
        )
        usage.definition.properties = usage.definition.properties.filter((
          { name },
        ) => name !== property)
        if (!discriminant) {
          throw new Error(
            `type ${usage.definition.name} has no discriminant property ${property}`,
            { cause: { definition: usage.definition } },
          )
        }
        usage.definition.properties.unshift({
          title: discriminant.title,
          name: discriminant.name,
          description: discriminant.description,
          required: discriminant.required,
          type: "discriminant",
          value,
        })
      }
    }
  }

  const packages: Package[] = []
  for (const [path, methods] of Object.entries(OpenAPI.paths)) {
    for (const [method, operationSchema] of Object.entries(methods)) {
      const operation = parseOperation(path, method, operationSchema)
      const category = normalizeCategory(operation.category)
      let searchBound = packages
      let pack = null
      for (const component of category.split(".")) {
        pack = searchBound.find(({ category }) => category === component)
        if (!pack) {
          pack = {
            category: component,
            operations: [],
            entities: [],
            subpackages: [],
          }
          searchBound.push(pack)
        }
        searchBound = pack.subpackages
      }
      if (!pack) {
        throw new Error("category was empty", { cause: { operation } })
      }
      pack.operations.push(operation)
      shakeOperation(operation)
    }
  }
  for (const { definition, categories } of definitionUsages.values()) {
    const categoryList = [...categories].map(normalizeCategory)
    if (categoryList.length === 0) continue
    const category = categoryList.length === 1
      ? categoryList[0]
      : categoryList.every((category) => category.startsWith("platform"))
      ? "platform"
      : "common"
    let searchBound = packages
    let pack = null
    for (const component of category.split(".")) {
      pack = searchBound.find(({ category }) => category === component)
      if (!pack) {
        pack = {
          category: component,
          operations: [],
          entities: [],
          subpackages: [],
        }
        searchBound.push(pack)
      }
      searchBound = pack.subpackages
    }
    if (!pack) {
      throw new Error("category was empty", { cause: { definition } })
    }
    pack.entities.push(definition)
  }
  return sortPackages({
    category: "root",
    operations: [],
    entities: [],
    subpackages: packages,
  })
}

function sortPackages(pack: Package) {
  pack.subpackages.sort()
  for (const subpackage of pack.subpackages) {
    sortPackages(subpackage)
  }
  return pack
}
