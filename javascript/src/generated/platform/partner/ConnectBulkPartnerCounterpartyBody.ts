import type { PlatformPartnerFilterInput } from "./../../platform/PlatformPartnerFilterInput"
/**
 * 파트너 일괄 거래처 연동 요청 정보
 *
 * 파트너들을 일괄 거래처 연동합니다.
 */
export type ConnectBulkPartnerCounterpartyBody = {
	/** 일괄 거래처 연동할 파트너 조건 필터 */
	filter?: PlatformPartnerFilterInput
}
