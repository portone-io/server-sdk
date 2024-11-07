import type { PlatformSettlementFormulaPosition } from "./../platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaInvalidSyntax = {
	type: "INVALID_SYNTAX"
	syntax: string
	position: PlatformSettlementFormulaPosition
}
