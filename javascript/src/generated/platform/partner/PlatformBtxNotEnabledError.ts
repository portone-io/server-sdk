/** BTX 기능이 활성화되지 않아 요청을 처리할 수 없는 경우 */
export type PlatformBtxNotEnabledError = {
	type: "PLATFORM_BTX_NOT_ENABLED"
	message?: string
}
