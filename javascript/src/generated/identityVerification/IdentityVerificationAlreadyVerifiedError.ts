/** 본인인증 건이 이미 인증 완료된 상태인 경우 */
export type IdentityVerificationAlreadyVerifiedError = {
	type: "IDENTITY_VERIFICATION_ALREADY_VERIFIED"
	message?: string
}
