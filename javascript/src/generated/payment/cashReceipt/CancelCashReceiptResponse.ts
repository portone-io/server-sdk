/** 현금 영수증 취소 성공 응답 */
export type CancelCashReceiptResponse = {
	/**
	 * 취소 금액
	 * (int64)
	 */
	cancelledAmount: number
	/**
	 * 현금 영수증 취소 완료 시점
	 * (RFC 3339 date-time)
	 */
	cancelledAt: string
}
