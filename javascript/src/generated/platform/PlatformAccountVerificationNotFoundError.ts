/** 파트너 계좌 검증 아이디를 찾을 수 없는 경우 */
export type PlatformAccountVerificationNotFoundError = {
	type: "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND"
	message?: string
}
