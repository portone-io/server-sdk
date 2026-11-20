/** 결제 세션이 존재하지 않는 경우 */
export type SessionNotFoundError = {
	type: "SESSION_NOT_FOUND"
	message?: string
}
