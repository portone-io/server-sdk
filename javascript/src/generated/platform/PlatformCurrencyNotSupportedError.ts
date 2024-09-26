/** 지원 되지 않는 통화를 선택한 경우 */
export type PlatformCurrencyNotSupportedError = {
	type: "PLATFORM_CURRENCY_NOT_SUPPORTED"
	message?: string
}
