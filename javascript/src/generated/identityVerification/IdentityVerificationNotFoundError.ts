/** 요청된 본인인증 건이 존재하지 않는 경우 */
export type IdentityVerificationNotFoundError = {
	type: "IDENTITY_VERIFICATION_NOT_FOUND"
	message?: string
}
