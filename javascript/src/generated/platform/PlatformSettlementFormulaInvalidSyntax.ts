import type { PlatformSettlementFormulaPosition } from "#generated/platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaInvalidSyntax = {
	type: "INVALID_SYNTAX"
	syntax: string
	position: PlatformSettlementFormulaPosition
}
