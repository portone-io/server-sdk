import type { PlatformSettlementFormulaPosition } from "./../platform/PlatformSettlementFormulaPosition"
export type PlatformSettlementFormulaUnsupportedVariable = {
	type: "UNSUPPORTED_VARIABLE"
	name: string
	position: PlatformSettlementFormulaPosition
}
