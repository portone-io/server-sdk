/** 결제 금액 세부 정보 */
export type PaymentAmount = {
	/**
	 * 총 결제금액
	 * (int64)
	 */
	total: number
	/**
	 * 면세액
	 * (int64)
	 */
	taxFree: number
	/**
	 * 부가세액
	 * (int64)
	 */
	vat?: number
	/**
	 * 공급가액
	 * (int64)
	 */
	supply?: number
	/**
	 * 할인금액
	 *
	 * 카드사 프로모션, 포트원 프로모션, 적립형 포인트 결제, 쿠폰 할인 등을 포함합니다.
	 * (int64)
	 */
	discount: number
	/**
	 * 실제 결제금액
	 * (int64)
	 */
	paid: number
	/**
	 * 취소금액
	 * (int64)
	 */
	cancelled: number
	/**
	 * 취소금액 중 면세액
	 * (int64)
	 */
	cancelledTaxFree: number
}
