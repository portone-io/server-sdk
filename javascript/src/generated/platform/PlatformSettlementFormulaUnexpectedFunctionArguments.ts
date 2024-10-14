import type { PlatformSettlementFormulaPosition } from "#generated/platform/PlatformSettlementFormulaPosition"

export type PlatformSettlementFormulaUnexpectedFunctionArguments = {
	type: "UNEXPECTED_FUNCTION_ARGUMENTS"
	functionName: string
	/** (int32) */
	expectedCount: number
	/** (int32) */
	currentCount: number
	position: PlatformSettlementFormulaPosition
}