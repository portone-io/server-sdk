/** 지원하지 않는 은행인 경우 */
export type PlatformNotSupportedBankError = {
	type: "PLATFORM_NOT_SUPPORTED_BANK"
	message?: string
}
