import type { PlatformBulkPayoutFilterInputCriteria } from "#generated/platform/bulkPayout/PlatformBulkPayoutFilterInputCriteria"
import type { PlatformBulkPayoutStatus } from "#generated/platform/bulkPayout/PlatformBulkPayoutStatus"
import type { PlatformPayoutMethod } from "#generated/platform/PlatformPayoutMethod"

export type PlatformBulkPayoutFilterInput = {
	statuses?: PlatformBulkPayoutStatus[]
	methods?: PlatformPayoutMethod[]
	criteria?: PlatformBulkPayoutFilterInputCriteria
}
