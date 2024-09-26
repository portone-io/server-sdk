import type { PageInput } from "#generated/common/PageInput"
import type { PlatformBulkPayoutPartnerSettlementsFilterInput } from "#generated/platform/PlatformBulkPayoutPartnerSettlementsFilterInput"

export type GetPlatformBulkPayoutPartnerSettlementsBody = {
	filter?: PlatformBulkPayoutPartnerSettlementsFilterInput
	page?: PageInput
	isForTest?: boolean
}
