/** 정산 가능한 금액을 초과한 경우 */
export type PlatformSettlementAmountExceededError = {
	type: "PLATFORM_SETTLEMENT_AMOUNT_EXCEEDED"
	message?: string
	/**
	 * 상품 아이디
	 *
	 * 주문 항목의 상품 아이디입니다.
	 */
	productId?: string
	/**
	 * 요청 받은 금액
	 * (int64)
	 */
	requestedAmount: number
	/**
	 * 초과한 금액
	 * (int64)
	 */
	allowedAmount: number
}
