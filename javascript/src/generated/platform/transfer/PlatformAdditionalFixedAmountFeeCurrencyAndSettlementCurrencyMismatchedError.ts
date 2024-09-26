import type { Currency } from "#generated/common/Currency"

export type PlatformAdditionalFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError = {
	type: "PLATFORM_ADDITIONAL_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"
	id: string
	graphqlId: string
	feeCurrency: Currency
	settlementCurrency: Currency
	message?: string
}
