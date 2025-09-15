import type { PlatformPartnerFilterInput } from "./../../platform/PlatformPartnerFilterInput"
/**
 * 파트너 일괄 국세청 연동 해제 요청 정보
 *
 * 파트너들을 일괄 국세청 연동 해제합니다.
 */
export type DisconnectBulkPartnerMemberCompanyBody = {
	/** 일괄 국세청 연동 해제할 파트너 조건 필터 */
	filter?: PlatformPartnerFilterInput
}
