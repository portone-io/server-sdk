/** 유효하지 않은 결제 토큰인 경우 */
export type InvalidPaymentTokenError = {
	type: "INVALID_PAYMENT_TOKEN"
	message?: string
}
