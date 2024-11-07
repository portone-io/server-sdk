import * as fs from "@std/fs"
import * as path from "@std/path"
import { toPascalCase } from "@std/text"
import { makeCategoryMap, makeEntityMap } from "../common/maps.ts"
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

export function generateProject(projectRoot: string, pack: Package) {
  const srcPath = path.join(projectRoot, "src/portone_server_sdk/_generated")
  if (fs.existsSync(srcPath)) Deno.removeSync(srcPath, { recursive: true })
  const publicPath = path.join(projectRoot, "src/portone_server_sdk")
  fs.ensureDirSync(srcPath)
  const categoryMap = makeCategoryMap(pack)
  const entityMap = makeEntityMap(pack)
  const oneOfErrors = new Set<string>()
  const variantErrors = new Set<string>()
  collectErrors(pack, entityMap, oneOfErrors, variantErrors)
  generateErrors(
    srcPath,
    publicPath,
    [...variantErrors].toSorted(),
    categoryMap,
    entityMap,
  )
  generateEntityDirectory(srcPath, pack, categoryMap, entityMap)
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
}

function generateCategoryIndex(
  packagePath: string,
  publicPath: string,
  pack: Package,
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
  omitEntities: Set<string>,
  hierarchy: string = "portone_server_sdk._generated",
) {
  const hasClient = pack.operations.length > 0 || pack.subpackages.length > 0
  const crossRef = new Set<string>()
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
    writeClientObject(writer, pack, entityMap, crossRef, typing)
  }
  const importWriter = PythonWriter()
  importWriter.writeLine("from __future__ import annotations")
  if (hasClient) {
    importWriter.writeLine("import httpx")
    importWriter.writeLine("import json")
    importWriter.writeLine("from httpx import AsyncClient")
    typing.add("Optional")
  }
  const sortedTyping = [...typing].toSorted()
  if (sortedTyping.length > 0) {
    importWriter.writeLine(`from typing import ${sortedTyping.join(", ")}`)
  }
  const sortedRef = [...crossRef].toSorted()
  for (const ref of sortedRef) {
    const category = categoryMap.get(ref)
    if (!category) {
      throw new Error("unrecognized category", { cause: { ref } })
    }
    importWriter.writeLine(
      `from portone_server_sdk._generated.${
        category.split(".").map(toSnakeCase).join(".")
      }.${toSnakeCase(ref)} import ${ref}, _deserialize_${
        toSnakeCase(ref)
      }, _serialize_${toSnakeCase(ref)}`,
    )
  }
  if (hasClient) {
    importWriter.writeLine("from urllib.parse import quote")
    for (const subpackage of pack.subpackages) {
      if (
        subpackage.operations.length > 0 || subpackage.subpackages.length > 0
      ) {
        importWriter.writeLine(
          `from .${toSnakeCase(subpackage.category)} import ${
            toPascalCase(subpackage.category)
          }Client`,
        )
      }
    }
    importWriter.writeLine(`from portone_server_sdk._generated import errors`)
  }
  const indexPath = path.join(packagePath, "__init__.py")
  Deno.writeTextFileSync(indexPath, importWriter.content + writer.content)

  const publicWriter = PythonWriter()
  const all = []
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
      `from portone_server_sdk._generated.${
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
      `from ${hierarchy} import ${toPascalCase(pack.category)}Client`,
    )
    all.push(`${toPascalCase(pack.category)}Client`)
  }
  if (pack.category !== "root" && pack.category !== "webhook") {
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
  typing: Set<string>,
) {
  const subpackages = pack.subpackages.filter(({ operations, subpackages }) =>
    operations.length > 0 || subpackages.length > 0
  )
  implWriter.writeLine(`class ${toPascalCase(pack.category)}Client:`)
  implWriter.indent()
  implWriter.writeLine("_secret: str")
  implWriter.writeLine("_user_agent: str")
  implWriter.writeLine("_base_url: str")
  implWriter.writeLine("_store_id: Optional[str]")
  implWriter.writeLine("_client: AsyncClient")
  for (const subpackage of subpackages) {
    implWriter.writeLine(
      `${toSnakeCase(subpackage.category)}: ${
        toPascalCase(subpackage.category)
      }Client`,
    )
  }
  implWriter.writeLine("")
  implWriter.writeLine(
    "def __init__(self, secret: str, user_agent: str, base_url: str, store_id: Optional[str]):",
  )
  implWriter.indent()
  implWriter.writeLine("self._secret = secret")
  implWriter.writeLine("self._user_agent = user_agent")
  implWriter.writeLine("self._base_url = base_url")
  implWriter.writeLine("self._store_id = store_id")
  implWriter.writeLine("self._client = AsyncClient()")
  for (const subpackage of subpackages) {
    implWriter.writeLine(
      `self.${toSnakeCase(subpackage.category)} = ${
        toPascalCase(subpackage.category)
      }Client(secret, user_agent, base_url, store_id)`,
    )
  }
  implWriter.outdent()
  for (const operation of pack.operations) {
    writeOperation(
      implWriter,
      operation,
      entityMap,
      crossRef,
      typing,
      false,
    )
    writeOperation(
      implWriter,
      operation,
      entityMap,
      crossRef,
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
  variantErrors: Set<string>,
) {
  for (const operation of pack.operations) {
    oneOfErrors.add(operation.errors)
    const errorEntity = entityMap.get(operation.errors)
    if (!errorEntity) {
      throw new Error("unrecognized error", { cause: { operation } })
    }
    switch (errorEntity.type) {
      case "object":
        variantErrors.add(errorEntity.name)
        break
      case "oneOf":
        for (const variant of errorEntity.variants) {
          variantErrors.add(variant.name)
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
    collectErrors(subpackage, entityMap, oneOfErrors, variantErrors)
  }
}

const PortOneError = `
@dataclass(init=False)
class PortOneError(Exception):
    """포트원 SDK에서 발생하는 모든 에러의 기본 타입입니다."""

    message: Optional[str] = field(init=False)

@dataclass
class UnknownError(PortOneError):
    """알 수 없는 경우"""

    message: Optional[str] = field(default="알 수 없는 오류가 발생했습니다.", init=False)
    error: dict
`

function generateErrors(
  srcPath: string,
  publicPath: string,
  errors: string[],
  categoryMap: Map<string, string>,
  entityMap: Map<string, Definition>,
) {
  const writer = PythonWriter()
  writer.writeLine("from __future__ import annotations")
  writer.writeLine("from dataclasses import InitVar, dataclass, field")
  writer.writeLine("from typing import Optional")
  const crossRef = new Set<string>()
  for (const error of errors) {
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
      `from portone_server_sdk._generated.${path}.${
        toSnakeCase(error)
      } import ${error} as Internal${error}`,
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
      `from portone_server_sdk._generated.${path}.${
        toSnakeCase(ref)
      } import ${ref}`,
    )
  }
  for (const line of PortOneError.split("\n")) {
    writer.writeLine(line)
  }
  for (const error of errors) {
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
    writer.writeLine(`class ${error}(PortOneError):`)
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
  const errorPath = path.join(srcPath, "errors.py")
  Deno.writeTextFileSync(errorPath, writer.content)
  const all = ["PortOneError", "UnknownError"].concat(errors).toSorted()
  const publicWriter = PythonWriter()
  publicWriter.writeLine(
    `from portone_server_sdk._generated.errors import ${all.join(", ")}`,
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
  writer.writeLine("from httpx import AsyncClient")
  for (const subpackage of pack.subpackages) {
    if (subpackage.operations.length > 0 || subpackage.subpackages.length > 0) {
      writer.writeLine(
        `from .${toSnakeCase(subpackage.category)} import ${
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
def __init__(self, *, secret: str, store_id: Optional[str] = None, base_url: str = "https://api.portone.io") -> None:
    """API Secret을 사용해 포트원 API 클라이언트를 생성합니다.
    """
    self._secret = secret
    self._store_id = store_id
    self._client = AsyncClient()
    user_agent = "__USER_AGENT__"
`

function writeRootClientObject(
  writer: Writer,
  pack: Package,
) {
  writer.writeLine("")
  writer.writeLine("class PortOneClient:")
  writer.indent()
  writer.writeLine("_secret: str")
  writer.writeLine("_store_id: Optional[str]")
  writer.writeLine("_base_url: str")
  writer.writeLine("_user_agent: str")
  writer.writeLine("_client: AsyncClient")
  const subpackages = pack.subpackages.filter(({ operations, subpackages }) =>
    operations.length > 0 || subpackages.length > 0
  )
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
      }Client(secret, user_agent, base_url, store_id)`,
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
) {
  fs.ensureDirSync(packagePath)
  for (const entity of pack.entities) {
    generateEntity(packagePath, categoryMap, entityMap, entity)
  }
  for (const subpackage of pack.subpackages) {
    generateEntityDirectory(
      path.join(packagePath, toSnakeCase(subpackage.category)),
      subpackage,
      categoryMap,
      entityMap,
    )
  }
}
