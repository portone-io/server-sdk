import type { Currency } from "#generated/common/Currency"

/** 정산 정보 */
export type Settlement = {
	/**
	 * PG 수수료 요금
	 * (int64)
	 */
	feeAmount: number
	/**
	 * PG 수수료 부가세
	 * (int64)
	 */
	feeVatAmount: number
	/**
	 * 정산 금액
	 * (int64)
	 */
	settlementAmount: number
	/** 정산 통화 */
	settlementCurrency: Currency
	/**
	 * 정산일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 */
	settlementDate: string
}
