import type { PlatformCompanyState } from "./../../platform/company/PlatformCompanyState"
/** 사업자 조회 성공 응답 정보 */
export type GetPlatformCompanyStatePayload = {
	/** 사업자 정보 */
	companyState: PlatformCompanyState
	/** 사업자 검증 아이디 */
	companyVerificationId: string
}
