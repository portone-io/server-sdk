/** 요청이 거절된 경우 */
export type ForbiddenError = {
	type: "FORBIDDEN"
	message?: string
}
