import type { PageInfo } from "#generated/common/PageInfo"
import type { PlatformPayout } from "#generated/platform/payout/PlatformPayout"
import type { PlatformPayoutStatusStats } from "#generated/platform/PlatformPayoutStatusStats"

export type GetPlatformPayoutsResponse = {
	items: PlatformPayout[]
	page: PageInfo
	counts: PlatformPayoutStatusStats
}
