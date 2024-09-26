/** 외부 api의 일시적인 오류 */
export type PlatformExternalApiTemporarilyFailedError = {
	type: "PLATFORM_EXTERNAL_API_TEMPORARILY_FAILED"
	message?: string
}
