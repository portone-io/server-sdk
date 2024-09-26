/** 결제가 완료되지 않은 경우 */
export type PaymentNotPaidError = {
	type: "PAYMENT_NOT_PAID"
	message?: string
}
