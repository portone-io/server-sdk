/** 결제가 이미 완료된 경우 */
export type AlreadyPaidError = {
	type: "ALREADY_PAID"
	message?: string
}
