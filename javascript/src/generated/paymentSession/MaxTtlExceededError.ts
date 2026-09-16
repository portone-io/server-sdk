/** 요청된 TTL이 정책 상한을 초과한 경우 */
export type MaxTtlExceededError = {
	type: "MAX_TTL_EXCEEDED"
	message?: string
}
