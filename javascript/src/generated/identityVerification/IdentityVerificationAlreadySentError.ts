/** 본인인증 건이 이미 API로 요청된 상태인 경우 */
export type IdentityVerificationAlreadySentError = {
	type: "IDENTITY_VERIFICATION_ALREADY_SENT"
	message?: string
}
