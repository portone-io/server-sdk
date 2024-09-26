/** 인증 정보가 올바르지 않은 경우 */
export type UnauthorizedError = {
	type: "UNAUTHORIZED"
	message?: string
}
