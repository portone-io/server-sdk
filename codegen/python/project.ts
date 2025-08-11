import * as fs from "@std/fs"
import * as path from "@std/path"
import { toPascalCase } from "@std/text"
import { makeCategoryMap, makeEntityMap } from "../common/maps.ts"
import { isClientPackage } from "../common/package.ts"
import { entities as webhookEntities } from "../common/webhook/index.ts"
import type { Writer } from "../common/writer.ts"
import type { Definition } from "../parser/definition.ts"
import type { Package } from "../parser/openapi.ts"
import {
  filterName,
  intoInlineTypeName,
  PythonWriter,
  toSnakeCase,
} from "./common.ts"
import { writeDescription } from "./description.ts"
import { generateEntity } from "./entity.ts"
import { writeOperation } from "./operation.ts"
import { generateEntity as generateWebhookEntity } from "./webhook.ts"

export function generateProject(projectRoot: string, pack: Package) {
  const srcPath = path.join(projectRoot, "src/portone_server_sdk/_generated")
  if (fs.existsSync(srcPath)) Deno.removeSync(srcPath, { recursive: true })
  const publicPath = path.join(projectRoot, "src/portone_server_sdk")
  fs.ensureDirSync(srcPath)
  const categoryMap = makeCategoryMap(pack)
  const entityMap = makeEntityMap(pack)
  const oneOfErrors = new Set<string>()
  const variantErrors = new Map<string, Set<string>>()
  collectErrors(
    pack,
    entityMap,
    oneOfErrors,
    variantErrors,
    "",
  )
  generateErrors(
    srcPath,
    publicPath,
    variantErrors,
    categoryMap,
    entityMap,
  )
  generateEntityDirectory(srcPath, pack, categoryMap, entityMap)
  generateWebhook(srcPath)
  generateClient(srcPath, pack)
  const omitEntities = oneOfErrors.union(variantErrors)
  generateCategoryIndex(
    srcPath,
    publicPath,
    pack,
    categoryMap,
    entityMap,
    omitEntities,
  )
  generateIndex(path.join(projectRoot, "docs"), publicPath, pack)
}

function generateIndex(
  docsPath: string,
  srcPath: string,
  pack: Package,
) {
  const clients = Array<{ path: string; name: string }>()
  const collectClients = (pack: Package, hierarchy: string) => {
    for (const subpackage of pack.subpackages) {
      if (isClientPackage(subpackage)) {
        clients.push({
          path: `${hierarchy}.${toSnakeCase(subpackage.category)}`,
          name: `${toPascalCase(subpackage.category)}Client`,
        })
      }
      collectClients(
        subpackage,
        `${hierarchy}.${toSnakeCase(subpackage.category)}`,
      )
    }
  }
  collectClients(pack, "portone_server_sdk")
  clients.sort()
  const subpackages = pack.subpackages.map(({ category }) =>
    toSnakeCase(category)
  ).concat("webhook", "errors").toSorted()

  const all = subpackages.concat(clients.map(({ name }) => name)).concat(
    "PortOneClient",
  )

  const index = `${
    clients.map(({ path, name }) => `from ${path} import ${name}`).join("\n")
  }

from . import (
${subpackages.map((sub) => `    ${sub},`).join("\n")}
)

from ._generated.client import PortOneClient

__all__ = [
${all.toSorted().map((item) => `    "${item}",`).join("\n")}
]
`

  Deno.writeTextFileSync(path.join(srcPath, "__init__.py"), index)

  const rst = `portone_server_sdk
==================

.. currentmodule:: portone_server_sdk

.. autosummary::
   :toctree: _toctree
   :recursive:

${all.map((item) => `   ${item}`).join("\n")}
`
  Deno.writeTextFileSync(path.join(docsPath, "index.rst"), rst)
}

function generateWebhook(
  packagePath: string,
) {
  const webhookPath = path.join(packagePath, "webhook")
  fs.ensureDirSync(webhookPath)
  for (
    const entity of webhookEntities.toSorted((a, b) =>
      a.name.localeCompare(b.name)
    )
  ) {
    generateWebhookEntity(webhookPath, entity)
  }
}

function generateCategoryIndex(
  packagePath: string,
  publicPath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
  omitEntities: Set<string>,
  hierarchy: string = "",
) {
  const toRoot = ".".repeat(hierarchy.split(".").length)
  const hasClient = isClientPackage(pack)
  const crossRef = new Set<string>()
  const errorRef = new Set<string>()
  const writer = PythonWriter()
  for (const subpackage of pack.subpackages) {
    const subPath = path.join(packagePath, toSnakeCase(subpackage.category))
    fs.ensureDirSync(subPath)
    generateCategoryIndex(
      subPath,
      path.join(publicPath, toSnakeCase(subpackage.category)),
      subpackage,
      categoryMap,
      entityMap,
      omitEntities,
      `${hierarchy}.${toSnakeCase(subpackage.category)}`,
    )
  }
  const typing = new Set<string>()
  if (hasClient) {
    writeClientObject(writer, pack, entityMap, crossRef, errorRef, typing)
  }
  const importWriter = PythonWriter()
  importWriter.writeLine("from __future__ import annotations")
  if (hasClient) {
    importWriter.writeLine("import httpx")
    importWriter.writeLine("import json")
    importWriter.writeLine(
      "from httpx import AsyncClient, Client as SyncClient",
    )
    importWriter.writeLine(
      `from ${toRoot}._user_agent import USER_AGENT`,
    )
    typing.add("Optional")
  }
  const errors = pack.operations.map(({ errors }) => errors).toSorted()
  const sortedTyping = [...typing].toSorted()
  if (sortedTyping.length > 0) {
    importWriter.writeLine(`from typing import ${sortedTyping.join(", ")}`)
  }
  if (errorRef.size > 0) {
    const sortedError = [...errorRef].toSorted()
    importWriter.writeLine(
      `from ${toRoot}errors import ${sortedError.join(", ")}`,
    )
    for (const error of sortedError) {
      if (error === "UnknownError") continue
      const category = categoryMap.get(error)
      if (category == null) {
        throw new Error("unrecognized error ref", { cause: { ref: error } })
      }
      const canonicalCategory = category.split(".").map(toSnakeCase).join(".")
      importWriter.writeLine(
        `from ${toRoot}${canonicalCategory}.${
          toSnakeCase(error)
        } import _deserialize_${toSnakeCase(error)}`,
      )
    }
  }
  const sortedRef = [...crossRef].toSorted()
  for (const ref of sortedRef) {
    const category = categoryMap.get(ref)
    if (!category) {
      throw new Error("unrecognized category", { cause: { ref } })
    }
    importWriter.writeLine(
      `from ${toRoot}${category.split(".").map(toSnakeCase).join(".")}.${
        toSnakeCase(ref)
      } import ${ref}, _deserialize_${toSnakeCase(ref)}, _serialize_${
        toSnakeCase(ref)
      }`,
    )
  }
  if (hasClient) {
    importWriter.writeLine("from urllib.parse import quote")
    for (const subpackage of pack.subpackages) {
      if (
        isClientPackage(subpackage)
      ) {
        importWriter.writeLine(
          `from .${toSnakeCase(subpackage.category)}.client import ${
            toPascalCase(subpackage.category)
          }Client`,
        )
      }
    }
    if (pack.category !== "root") {
      const clientPath = path.join(packagePath, "client.py")
      Deno.writeTextFileSync(clientPath, importWriter.content + writer.content)
    }
  }

  const all = []
  const publicWriter = PythonWriter()
  if (errors.length > 0) {
    const errorPath = path.join(packagePath, "errors")
    fs.ensureDirSync(errorPath)
    for (const error of errors) {
      all.push(error)
      const errorWriter = PythonWriter()
      errorWriter.writeLine("from dataclasses import dataclass")
      errorWriter.writeLine(
        `from .${toRoot}._portone_error import PortOneError`,
      )
      errorWriter.writeLine("@dataclass")
      errorWriter.writeLine(`class ${error}(PortOneError):`)
      errorWriter.indent()
      errorWriter.writeLine("pass")
      errorWriter.outdent()
      Deno.writeTextFileSync(
        path.join(errorPath, `${toSnakeCase(error)}.py`),
        errorWriter.content,
      )
      publicWriter.writeLine(
        `from ${toRoot}_generated${hierarchy}.errors.${
          toSnakeCase(error)
        } import ${error}`,
      )
    }
  }
  for (const subpackage of pack.subpackages) {
    publicWriter.writeLine(`from . import ${toSnakeCase(subpackage.category)}`)
    all.push(toSnakeCase(subpackage.category))
  }
  const aliases = []
  for (const entity of pack.entities) {
    if (omitEntities.has(entity.name)) {
      continue
    }
    const category = categoryMap.get(entity.name)
    if (!category) {
      throw new Error("unrecognized category", { cause: { ref: entity.name } })
    }
    publicWriter.writeLine(
      `from ${toRoot}_generated.${
        category.split(".").map(toSnakeCase).join(".")
      }.${toSnakeCase(entity.name)} import ${entity.name}`,
    )
    if (entity.type !== "object") {
      aliases.push(entity.name)
    }
    all.push(entity.name)
  }
  if (hasClient) {
    publicWriter.writeLine(
      `from ${toRoot}_generated${hierarchy}.client import ${
        toPascalCase(pack.category)
      }Client`,
    )
    all.push(`${toPascalCase(pack.category)}Client`)
  }
  if (pack.category !== "root") {
    publicWriter.writeLine("__all__ = [")
    publicWriter.indent()
    for (const item of all) {
      publicWriter.writeLine(`"${item}",`)
    }
    publicWriter.outdent()
    publicWriter.writeLine("]")
    fs.ensureDirSync(publicPath)
    Deno.writeTextFileSync(
      path.join(publicPath, "__init__.py"),
      publicWriter.content,
    )
  }
}

function writeClientObject(
  implWriter: Writer,
  pack: Package,
  entityMap: Map<string, Definition>,
  crossRef: Set<string>,
  errorRef: Set<string>,
  typing: Set<string>,
) {
  const subpackages = pack.subpackages.filter(isClientPackage)
  implWriter.writeLine(`class ${toPascalCase(pack.category)}Client:`)
  implWriter.indent()
  implWriter.writeLine("_secret: str")
  implWriter.writeLine("_base_url: str")
  implWriter.writeLine("_store_id: Optional[str]")
  implWriter.writeLine("_async_client: AsyncClient")
  implWriter.writeLine("_sync_client: SyncClient")
  for (const subpackage of subpackages) {
    implWriter.writeLine(
      `${toSnakeCase(subpackage.category)}: ${
        toPascalCase(subpackage.category)
      }Client`,
    )
  }
  implWriter.writeLine("")
  implWriter.writeLine(
    `def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None):`,
  )
  implWriter.indent()
  implWriter.writeLine(
    `"""`,
  )
  implWriter.writeLine(
    "API Secret을 사용해 포트원 API 클라이언트를 생성합니다.",
  )
  implWriter.writeLine("")
  implWriter.writeLine("Args:")
  implWriter.indent()
  implWriter.writeLine("secret (str): 포트원 API Secret입니다.")
  implWriter.writeLine(
    `base_url (str, optional): 포트원 REST API 주소입니다. 기본값은 \`"https://api.portone.io"\`입니다.`,
  )
  implWriter.writeLine(
    `store_id: 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.`,
  )
  implWriter.writeLine(`"""`)
  implWriter.outdent()
  implWriter.writeLine("self._secret = secret")
  implWriter.writeLine("self._base_url = base_url")
  implWriter.writeLine("self._store_id = store_id")
  implWriter.writeLine("self._async_client = AsyncClient(timeout=60.0)")
  implWriter.writeLine("self._sync_client = SyncClient(timeout=60.0)")
  for (const subpackage of subpackages) {
    implWriter.writeLine(
      `self.${toSnakeCase(subpackage.category)} = ${
        toPascalCase(subpackage.category)
      }Client(secret=secret, base_url=base_url, store_id=store_id)`,
    )
  }
  implWriter.outdent()
  for (const operation of pack.operations) {
    writeOperation(
      implWriter,
      operation,
      entityMap,
      crossRef,
      errorRef,
      typing,
      false,
    )
    writeOperation(
      implWriter,
      operation,
      entityMap,
      crossRef,
      errorRef,
      typing,
      true,
    )
  }
  implWriter.outdent()
}

function collectErrors(
  pack: Package,
  entityMap: Map<string, Definition>,
  oneOfErrors: Set<string>,
  variantErrors: Map<string, Set<string>>,
  hierarchy: string,
) {
  for (const operation of pack.operations) {
    oneOfErrors.add(operation.errors)
    const errorEntity = entityMap.get(operation.errors)
    if (!errorEntity) {
      throw new Error("unrecognized error", { cause: { operation } })
    }
    switch (errorEntity.type) {
      case "object": {
        let parents = variantErrors.get(errorEntity.name)
        if (parents == null) {
          parents = new Set()
          variantErrors.set(errorEntity.name, parents)
        }
        break
      }
      case "oneOf":
        for (const variant of errorEntity.variants) {
          let parents = variantErrors.get(variant.name)
          if (parents == null) {
            parents = new Set()
            variantErrors.set(variant.name, parents)
          }
          parents.add(`${hierarchy}.errors.${errorEntity.name}`)
        }
        break
      case "string":
      case "number":
      case "boolean":
      case "ref":
      case "discriminant":
      case "enum":
      case "array":
      case "integer":
        continue
      default:
        throw new Error("unrecognized error type", {
          cause: { error: errorEntity },
        })
    }
  }
  for (const subpackage of pack.subpackages) {
    collectErrors(
      subpackage,
      entityMap,
      oneOfErrors,
      variantErrors,
      `${hierarchy}.${toSnakeCase(subpackage.category)}`,
    )
  }
}

function generateErrors(
  srcPath: string,
  publicPath: string,
  errors: Map<string, Set<string>>,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  const writer = PythonWriter()
  writer.writeLine("from __future__ import annotations")
  writer.writeLine("from dataclasses import InitVar, dataclass, field")
  writer.writeLine("from typing import Optional")
  const crossRef = new Set<string>()
  for (const error of errors.keys()) {
    const path = categoryMap.get(error)?.split(".")?.map(toSnakeCase)?.join(".")
    if (!path) {
      throw new Error("unrecognized error reference", { cause: { error } })
    }
    const definition = entityMap.get(error)
    if (!definition) {
      throw new Error("unrecognized error reference", { cause: { error } })
    }
    if (definition.type !== "object") {
      throw new Error("unsupported generation of error type", {
        cause: { definition },
      })
    }
    for (const property of definition.properties) {
      switch (property.type) {
        case "ref":
          crossRef.add(property.value)
          break
        case "oneOf":
          for (const { name } of property.variants) {
            crossRef.add(name)
          }
          break
        case "array":
          switch (property.item.type) {
            case "ref":
              crossRef.add(property.item.value)
              break
            case "string":
            case "number":
            case "boolean":
            case "oneOf":
            case "discriminant":
            case "enum":
            case "integer":
              break
            case "object":
            case "array":
              throw new Error("unsupported error property array item type", {
                cause: { definition },
              })
            default:
              throw new Error("unsupported definition type", {
                cause: { definition: property.item },
              })
          }
          break
        case "string":
        case "number":
        case "boolean":
        case "discriminant":
        case "enum":
        case "integer":
          break
        case "object":
          throw new Error("unsupported error property type", {
            cause: { definition },
          })
      }
    }
    writer.writeLine(
      `from .${path}.${toSnakeCase(error)} import ${error} as Internal${error}`,
    )
  }
  const allParents = [
    ...errors.values().reduce((prev, current) => prev.union(current)),
  ].toSorted()
  for (const parent of allParents) {
    const dot = parent.lastIndexOf(".")
    const name = parent.slice(dot + 1)
    const module = parent.slice(undefined, dot)
    writer.writeLine(
      `from ${module}.${toSnakeCase(name)} import ${name}`,
    )
  }
  const sortedRef = [...crossRef].toSorted()
  for (const ref of sortedRef) {
    const path = categoryMap.get(ref)?.split(".")?.map(toSnakeCase)?.join(".")
    if (!path) {
      throw new Error("unrecognized error property reference", {
        cause: { ref },
      })
    }
    writer.writeLine(
      `from .${path}.${toSnakeCase(ref)} import ${ref}`,
    )
  }
  for (const [error, parents] of errors.entries()) {
    const definition = entityMap.get(error)
    if (!definition) {
      throw new Error("unrecognized error reference", { cause: { error } })
    }
    if (definition.type !== "object") {
      throw new Error("unsupported generation of error type", {
        cause: { definition },
      })
    }
    const additionalProperties = definition.properties.filter(({ name }) =>
      name !== "type"
    )
    writer.writeLine("")
    writer.writeLine("@dataclass")
    const extension = [...parents].map((hierarchy) =>
      hierarchy.split(".").at(-1)!
    ).toSorted().join(", ")
    writer.writeLine(`class ${error}(${extension}):`)
    writer.indent()
    writeDescription(writer, definition.description)
    for (const property of additionalProperties) {
      if (property.name === "message") continue
      const inlineType = intoInlineTypeName(property)
      const type = property.required ? inlineType : `Optional[${inlineType}]`
      writer.writeLine(
        `${filterName(property.name)}: ${type} = field(init=False)`,
      )
    }
    writer.writeLine(`_error: InitVar[Internal${error}]`)
    writer.writeLine("")
    writer.writeLine(
      `def __post_init__(self, _error: Internal${error}) -> None:`,
    )
    writer.indent()
    for (const property of additionalProperties) {
      const name = filterName(property.name)
      writer.writeLine(`self.${name} = _error.${name}`)
    }
    writer.outdent()
    writer.outdent()
  }
  writer.writeLine("@dataclass")
  writer.writeLine(
    `class UnknownError(${
      allParents.map((hierarchy) => hierarchy.split(".").at(-1)!).join(", ")
    }):`,
  )
  writer.indent()
  writer.writeLine(`"""알 수 없는 경우"""`)
  writer.writeLine(
    `message: Optional[str] = field(default="알 수 없는 오류가 발생했습니다.", init=False)`,
  )
  writer.writeLine("error: dict")
  writer.outdent()
  const errorPath = path.join(srcPath, "errors.py")
  Deno.writeTextFileSync(errorPath, writer.content)
  const importErrors = [...errors.keys(), "UnknownError"].toSorted()
  const all = ["PortOneError"].concat(importErrors)
  const publicWriter = PythonWriter()
  publicWriter.writeLine(
    `from ._generated.errors import ${importErrors.join(", ")}`,
  )
  publicWriter.writeLine(
    "from ._portone_error import PortOneError",
  )
  publicWriter.writeLine("__all__ = [")
  publicWriter.indent()
  for (const item of all) {
    publicWriter.writeLine(`"${item}",`)
  }
  publicWriter.outdent()
  publicWriter.writeLine("]")
  Deno.writeTextFileSync(
    path.join(publicPath, "errors.py"),
    publicWriter.content,
  )
}

function generateClient(
  srcPath: string,
  pack: Package,
) {
  const writer = PythonWriter()
  writer.writeLine("from __future__ import annotations")
  writer.writeLine("from typing import Optional")
  for (const subpackage of pack.subpackages) {
    if (isClientPackage(subpackage)) {
      writer.writeLine(
        `from .${toSnakeCase(subpackage.category)}.client import ${
          toPascalCase(subpackage.category)
        }Client`,
      )
    }
  }
  writeRootClientObject(writer, pack)
  const operationPath = path.join(srcPath, "client.py")
  Deno.writeTextFileSync(operationPath, writer.content)
}

const PortOneClientInit = `
def __init__(self, *, secret: str, base_url: str = "https://api.portone.io", store_id: Optional[str] = None) -> None:
    """
    API Secret을 사용해 포트원 API 클라이언트를 생성합니다.

    Args:
        secret (str): 포트원 API Secret입니다.")
        base_url (str, optional): 포트원 REST API 주소입니다. 기본값은 \`"https://api.portone.io"\`입니다.
        store_id (str, optional): 하위 상점에 대해 기능을 사용할 때 필요한 하위 상점의 ID입니다.
    """
`

function writeRootClientObject(
  writer: Writer,
  pack: Package,
) {
  writer.writeLine("")
  writer.writeLine("class PortOneClient:")
  writer.indent()
  const subpackages = pack.subpackages.filter(isClientPackage)
  for (const subpackage of subpackages) {
    writer.writeLine(
      `${toSnakeCase(subpackage.category)}: ${
        toPascalCase(subpackage.category)
      }Client`,
    )
  }
  for (const line of PortOneClientInit.split("\n")) {
    writer.writeLine(line)
  }
  writer.indent()
  for (const subpackage of subpackages) {
    writer.writeLine(
      `self.${toSnakeCase(subpackage.category)} = ${
        toPascalCase(subpackage.category)
      }Client(secret=secret, base_url=base_url, store_id=store_id)`,
    )
  }
  writer.outdent()
  writer.outdent()
}

function generateEntityDirectory(
  packagePath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
  depth: number = 1,
) {
  fs.ensureDirSync(packagePath)
  for (const entity of pack.entities) {
    generateEntity(packagePath, categoryMap, entityMap, entity, depth)
  }
  for (const subpackage of pack.subpackages) {
    generateEntityDirectory(
      path.join(packagePath, toSnakeCase(subpackage.category)),
      subpackage,
      categoryMap,
      entityMap,
      depth + 1,
    )
  }
}
