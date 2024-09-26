import type { PageInfo } from "#generated/common/PageInfo"
import type { PlatformBulkPayout } from "#generated/platform/bulkPayout/PlatformBulkPayout"
import type { PlatformBulkPayoutStatusStats } from "#generated/platform/bulkPayout/PlatformBulkPayoutStatusStats"

export type GetPlatformBulkPayoutsResponse = {
	items: PlatformBulkPayout[]
	page: PageInfo
	counts: PlatformBulkPayoutStatusStats
}
