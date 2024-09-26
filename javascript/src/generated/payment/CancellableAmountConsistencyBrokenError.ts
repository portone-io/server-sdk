/** 취소 가능 잔액 검증에 실패한 경우 */
export type CancellableAmountConsistencyBrokenError = {
	type: "CANCELLABLE_AMOUNT_CONSISTENCY_BROKEN"
	message?: string
}
