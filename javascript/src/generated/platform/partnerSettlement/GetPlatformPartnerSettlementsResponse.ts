import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformPartnerSettlement } from "./../../platform/partnerSettlement/PlatformPartnerSettlement"
import type { PlatformPartnerSettlementStatusStats } from "./../../platform/partnerSettlement/PlatformPartnerSettlementStatusStats"

/** 정산내역 다건 조회 성공 응답 정보 */
export type GetPlatformPartnerSettlementsResponse = {
	/** 조회된 정산내역 리스트 */
	items: PlatformPartnerSettlement[]
	/** 조회된 페이지 정보 */
	page: PageInfo
	/** 정산내역 상태 별 갯수 */
	counts: PlatformPartnerSettlementStatusStats
}
