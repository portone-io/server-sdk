/** 사업자 정보를 찾을 수 없는 경우 */
export type PlatformCompanyNotFoundError = {
	type: "PLATFORM_COMPANY_NOT_FOUND"
	message?: string
}
