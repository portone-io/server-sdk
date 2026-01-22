/** 결제 취소 내역이 취소 요청 상태가 아닌 경우 */
export type PaymentCancellationNotPendingError = {
	type: "PAYMENT_CANCELLATION_NOT_PENDING"
	message?: string
}
