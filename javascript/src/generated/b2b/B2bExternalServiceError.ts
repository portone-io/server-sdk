/** 외부 서비스에서 에러가 발생한 경우 */
export type B2bExternalServiceError = {
	type: "B2B_EXTERNAL_SERVICE"
	message: string
}
