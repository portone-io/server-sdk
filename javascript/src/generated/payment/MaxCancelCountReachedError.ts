/** 취소 시도 횟수가 초과된 경우 */
export type MaxCancelCountReachedError = {
	type: "MAX_CANCEL_COUNT_REACHED"
	message?: string
}
