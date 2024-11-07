import type { PageInput } from "./../../common/PageInput"
import type { PlatformPartnerSettlementFilterInput } from "./../../platform/partnerSettlement/PlatformPartnerSettlementFilterInput"

/** 정산내역 다건 조회를 위한 입력 정보 */
export type GetPlatformPartnerSettlementsBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 정산내역 조건 필터 */
	filter: PlatformPartnerSettlementFilterInput
	isForTest: boolean
}
