/** 카카오페이 주문 조회 응답 */
export type GetKakaopayPaymentOrderResponse = {
	/**
	 * HTTP 상태 코드
	 * (int32)
	 */
	statusCode: number
	/** HTTP 응답 본문 (JSON) */
	body: string
}
