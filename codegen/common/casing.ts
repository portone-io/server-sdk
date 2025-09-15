import {
  toCamelCase as toCamelCaseDeno,
  toPascalCase as toPascalCaseDeno,
  toSnakeCase as toSnakeCaseDeno,
} from "@std/text"

export function toSnakeCase(name: string): string {
  return toSnakeCaseDeno(name).replaceAll("b_2_b", "b2b")
}

export function toCamelCase(text: string): string {
  return toCamelCaseDeno(text).replaceAll("b2B", "b2b")
}

export function toPascalCase(text: string): string {
  return toPascalCaseDeno(text).replaceAll("B2B", "B2b")
}
