/** 품목 */
export type B2bTaxInvoiceItem = {
	/**
	 * 결제일
	 *
	 * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
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
	 * 입력 범위 : -99999999.99 ~ 999999999.99, 10^-quantityScale 단위로 치환됨
	 * (int64)
	 */
	quantity?: number
	/**
	 * 수량 단위
	 *
	 * 입력 범위 : 0 ~ 2, 기본값: 0
	 * (int32)
	 */
	quantityScale?: number
	/**
	 * 단가
	 *
	 * 입력 범위 : -99999999999999.99 ~ 999999999999999.99
	 * (int64)
	 */
	unitCostAmount?: number
	/**
	 * 단가 단위
	 *
	 * 입력 범위 : 0 ~ 2, 기본값: 0
	 * (int32)
	 */
	unitCostAmountScale?: number
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
