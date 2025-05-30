import type { B2bBusinessInfoResult } from "./../../platform/company/B2bBusinessInfoResult"
/** 사업자등록 정보 조회 성공 응답 */
export type GetB2bBusinessInfosResponse = {
	/** 사업자등록 정보 리스트 */
	result: B2bBusinessInfoResult[]
}
