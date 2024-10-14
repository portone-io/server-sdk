/** 결제 혹은 본인인증 시도 횟수가 최대에 도달한 경우 */
export type MaxTransactionCountReachedError = {
	type: "MAX_TRANSACTION_COUNT_REACHED"
	message?: string
}
