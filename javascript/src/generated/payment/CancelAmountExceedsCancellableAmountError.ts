/** 결제 취소 금액이 취소 가능 금액을 초과한 경우 */
export type CancelAmountExceedsCancellableAmountError = {
	type: "CANCEL_AMOUNT_EXCEEDS_CANCELLABLE_AMOUNT"
	message?: string
}
