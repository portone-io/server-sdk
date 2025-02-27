import type { PlatformPartnerFilterInput } from "./../../platform/PlatformPartnerFilterInput"
/**
 * 파트너 연동 사업자 일괄 연동 해제 요청 정보
 *
 * 파트너들을 연동 사업자에서 일괄 연동 해제합니다.
 */
export type DisconnectBulkPartnerMemberCompanyBody = {
	/** 연동 사업자에서 일괄 연동 해제할 파트너 조건 필터 */
	filter?: PlatformPartnerFilterInput
}
