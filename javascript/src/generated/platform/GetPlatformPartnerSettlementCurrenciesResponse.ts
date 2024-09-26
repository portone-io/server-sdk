import type { Currency } from "#generated/common/Currency"

/** 정산내역 통화 조회 결과 */
export type GetPlatformPartnerSettlementCurrenciesResponse = {
	/** 통화 단위 */
	settlementCurrencies: Currency[]
}
