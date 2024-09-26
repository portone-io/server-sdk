import type { PlatformSettlementFormulaPosition } from "#generated/platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaInvalidOperator = {
	type: "INVALID_OPERATOR"
	operator: string
	position: PlatformSettlementFormulaPosition
}
