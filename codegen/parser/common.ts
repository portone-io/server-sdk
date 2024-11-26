export function stripRefPrefix(ref: string): string {
  return ref.slice(ref.lastIndexOf("/") + 1)
}

export type Annotated = Partial<{
  title: string | null
  description: string | null
  format: string | null
}>
