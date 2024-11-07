import type { PageInput } from "./../../common/PageInput"
import type { PlatformBulkPayoutFilterInput } from "./../../platform/bulkPayout/PlatformBulkPayoutFilterInput"

export type GetPlatformBulkPayoutsBody = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformBulkPayoutFilterInput
}
