import type { Currency } from "./../../common/Currency"
export type PlatformContractPlatformFixedAmountFeeCurrencyAndSettlementCurrencyMismatchedError = {
	type: "PLATFORM_CONTRACT_PLATFORM_FIXED_AMOUNT_FEE_CURRENCY_AND_SETTLEMENT_CURRENCY_MISMATCHED"
	id: string
	graphqlId: string
	feeCurrency: Currency
	settlementCurrency: Currency
	message?: string
}
