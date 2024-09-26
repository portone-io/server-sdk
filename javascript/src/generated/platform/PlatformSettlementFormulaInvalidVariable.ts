import type { PlatformSettlementFormulaPosition } from "#generated/platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaInvalidVariable = {
	type: "INVALID_VARIABLE"
	name: string
	position: PlatformSettlementFormulaPosition
}
