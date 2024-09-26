import type { PlatformSettlementFormulaPosition } from "#generated/platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaUnsupportedVariable = {
	type: "UNSUPPORTED_VARIABLE"
	name: string
	position: PlatformSettlementFormulaPosition
}
