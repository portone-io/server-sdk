/** 결제가 이미 완료되었거나 대기중인 경우 */
export type AlreadyPaidOrWaitingError = {
	type: "ALREADY_PAID_OR_WAITING"
	message?: string
}
