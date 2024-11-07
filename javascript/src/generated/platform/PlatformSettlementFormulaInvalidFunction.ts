import type { PlatformSettlementFormulaPosition } from "./../platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaInvalidFunction = {
	type: "INVALID_FUNCTION"
	name: string
	position: PlatformSettlementFormulaPosition
}
