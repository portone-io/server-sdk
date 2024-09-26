/** 결제가 이미 취소된 경우 */
export type PaymentAlreadyCancelledError = {
	type: "PAYMENT_ALREADY_CANCELLED"
	message?: string
}
