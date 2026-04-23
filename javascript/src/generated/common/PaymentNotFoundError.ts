/** 결제 건이 존재하지 않는 경우 */
export type PaymentNotFoundError = {
	type: "PAYMENT_NOT_FOUND"
	message?: string
}
