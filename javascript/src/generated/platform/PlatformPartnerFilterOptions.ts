import type { PlatformPartnerContractSummary } from "./../platform/PlatformPartnerContractSummary"

/** 파트너 필터 옵션 조회 성공 응답 정보 */
export type PlatformPartnerFilterOptions = {
	/** 조회된 태그 리스트 */
	tags: string[]
	/** 조회된 파트너 계약 요약 정보 리스트 */
	contractSummary: PlatformPartnerContractSummary[]
}
