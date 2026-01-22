/** 결제 취소 내역이 존재하지 않는 경우 */
export type PaymentCancellationNotFoundError = {
	type: "PAYMENT_CANCELLATION_NOT_FOUND"
	message?: string
}
