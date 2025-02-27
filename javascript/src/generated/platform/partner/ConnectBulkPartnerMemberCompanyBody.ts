import type { PlatformPartnerFilterInput } from "./../../platform/PlatformPartnerFilterInput"
/**
 * 파트너 연동 사업자 일괄 연동 요청 정보
 *
 * 파트너들을 연동 사업자로 일괄 연동합니다.
 */
export type ConnectBulkPartnerMemberCompanyBody = {
	/** 연동 사업자로 일괄 연동할 파트너 조건 필터 */
	filter?: PlatformPartnerFilterInput
}
