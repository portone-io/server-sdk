import type { PlatformBulkPayoutFilterInputCriteria } from "./../../platform/bulkPayout/PlatformBulkPayoutFilterInputCriteria"
import type { PlatformBulkPayoutStatus } from "./../../platform/bulkPayout/PlatformBulkPayoutStatus"
import type { PlatformPayoutMethod } from "./../../platform/PlatformPayoutMethod"

export type PlatformBulkPayoutFilterInput = {
	statuses?: PlatformBulkPayoutStatus[]
	methods?: PlatformPayoutMethod[]
	criteria?: PlatformBulkPayoutFilterInputCriteria
}
