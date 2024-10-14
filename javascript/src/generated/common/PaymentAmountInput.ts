/** 금액 세부 입력 정보 */
export type PaymentAmountInput = {
	/**
	 * 총 금액
	 * (int64)
	 */
	total: number
	/**
	 * 면세액
	 * (int64)
	 */
	taxFree?: number
	/**
	 * 부가세액
	 *
	 * 고객사에서 직접 계산이 필요한 경우 입력합니다.
	 * 입력하지 않으면 면세 금액을 제외한 금액의 1/11 로 자동 계산됩니다.
	 * (int64)
	 */
	vat?: number
}