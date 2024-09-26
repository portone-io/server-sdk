export function stripRefPrefix(ref: string): string {
  return ref.slice(ref.lastIndexOf("/") + 1)
}
