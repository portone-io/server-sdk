import type { B2bBusinessInfo } from "./../../platform/company/B2bBusinessInfo"
/** 사업자등록 정보조회 결과 */
export type B2bBusinessInfoResult = {
	/** 사업자등록번호 */
	brn: string
	/** 사업자등록 정보 */
	businessInfo?: B2bBusinessInfo
	/** 조회 실패 시 에러 메시지 */
	error?: string
}
