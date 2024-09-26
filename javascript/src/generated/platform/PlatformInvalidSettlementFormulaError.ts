import type { PlatformSettlementFormulaError } from "#generated/platform/PlatformSettlementFormulaError"

export type PlatformInvalidSettlementFormulaError = {
	type: "PLATFORM_INVALID_SETTLEMENT_FORMULA"
	platformFee?: PlatformSettlementFormulaError
	discountShare?: PlatformSettlementFormulaError
	additionalFee?: PlatformSettlementFormulaError
	message?: string
}
