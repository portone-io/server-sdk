import type { PlatformSettlementFormulaPosition } from "./../platform/PlatformSettlementFormulaPosition"
export type PlatformSettlementFormulaInvalidOperator = {
	type: "INVALID_OPERATOR"
	operator: string
	position: PlatformSettlementFormulaPosition
}
