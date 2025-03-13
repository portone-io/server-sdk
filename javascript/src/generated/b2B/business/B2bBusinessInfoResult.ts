import type { B2bBusinessInfo } from "./../../b2B/business/B2bBusinessInfo"
/** 사업자 정보 조회 결과 */
export type B2bBusinessInfoResult = {
	/** 사업자등록번호 */
	brn: string
	/** 사업자 정보 */
	businessInfo?: B2bBusinessInfo
	/** 조회 실패 메시지 */
	error?: string
}
