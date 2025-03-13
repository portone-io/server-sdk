import type { B2bBusinessInfoResult } from "./../../b2B/business/B2bBusinessInfoResult"
/** 사업자 정보 다건 조회 성공 응답 */
export type GetB2bBusinessInfosResponse = {
	/** 사업자 정보 다건 조회 결과 리스트 */
	result: B2bBusinessInfoResult[]
}
