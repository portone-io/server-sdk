import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformBulkPayout } from "./../../platform/bulkPayout/PlatformBulkPayout"
import type { PlatformBulkPayoutStatusStats } from "./../../platform/bulkPayout/PlatformBulkPayoutStatusStats"
export type GetPlatformBulkPayoutsResponse = {
	items: PlatformBulkPayout[]
	page: PageInfo
	counts: PlatformBulkPayoutStatusStats
}
