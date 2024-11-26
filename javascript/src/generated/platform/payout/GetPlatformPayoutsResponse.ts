import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformPayout } from "./../../platform/payout/PlatformPayout"
import type { PlatformPayoutStatusStats } from "./../../platform/PlatformPayoutStatusStats"
export type GetPlatformPayoutsResponse = {
	items: PlatformPayout[]
	page: PageInfo
	counts: PlatformPayoutStatusStats
}
