/** 결제 세션이 만료된 경우 */
export type SessionExpiredError = {
	type: "SESSION_EXPIRED"
	message?: string
}
