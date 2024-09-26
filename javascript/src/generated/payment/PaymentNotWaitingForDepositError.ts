/** 결제 건이 입금 대기 상태가 아닌 경우 */
export type PaymentNotWaitingForDepositError = {
	type: "PAYMENT_NOT_WAITING_FOR_DEPOSIT"
	message?: string
}
