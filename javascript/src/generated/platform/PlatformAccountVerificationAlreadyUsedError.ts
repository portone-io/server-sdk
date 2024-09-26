/** 파트너 계좌 검증 아이디를 이미 사용한 경우 */
export type PlatformAccountVerificationAlreadyUsedError = {
	type: "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED"
	message?: string
}
