import type { Decimal } from "./../../b2b/taxInvoice/Decimal"
/** 품목 */
export type B2bTaxInvoiceItem = {
	/**
	 * 결제일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
	 * (yyyy-MM-dd)
	 */
	purchaseDate?: string
	/**
	 * 품명
	 *
	 * 최대 100자
	 */
	name?: string
	/**
	 * 규격
	 *
	 * 최대 100자
	 */
	spec?: string
	/**
	 * 수량
	 *
	 * 입력 범위 : -99999999.99 ~ 999999999.99
	 * `quantity.scale`의 입력 범위 : 0 ~ 2
	 * `quantity.value` * 10^-`quantity.scale` 단위로 치환됩니다.
	 */
	quantity?: Decimal
	/**
	 * 단가
	 *
	 * 입력 범위 : -99999999999999.99 ~ 999999999999999.99
	 * `unitCostAmount.scale`의 입력 범위 : 0 ~ 2
	 * `unitCostAmount.value` * 10^-`unitCostAmount.scale` 단위로 치환됩니다.
	 */
	unitCostAmount?: Decimal
	/**
	 * 공급가액
	 * (int64)
	 */
	supplyCostAmount?: number
	/**
	 * 세액
	 * (int64)
	 */
	taxAmount?: number
	/** 비고 */
	remark?: string
}
