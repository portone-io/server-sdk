import type { PlatformSettlementFormulaPosition } from "./../platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaInvalidVariable = {
	type: "INVALID_VARIABLE"
	name: string
	position: PlatformSettlementFormulaPosition
}
