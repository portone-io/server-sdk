import type { PageInfo } from "#generated/common/PageInfo"
import type { PlatformBulkPayoutPartnerSettlement } from "#generated/platform/PlatformBulkPayoutPartnerSettlement"
import type { PlatformPartnerSettlementStatusStats } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementStatusStats"

export type GetPlatformBulkPayoutPartnerSettlementsResponse = {
	items: PlatformBulkPayoutPartnerSettlement[]
	page: PageInfo
	counts: PlatformPartnerSettlementStatusStats
}
