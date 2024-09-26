/** 본인인증 건이 API로 요청된 상태가 아닌 경우 */
export type IdentityVerificationNotSentError = {
	type: "IDENTITY_VERIFICATION_NOT_SENT"
	message?: string
}
