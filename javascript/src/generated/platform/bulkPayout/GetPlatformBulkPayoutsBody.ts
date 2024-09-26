import type { PageInput } from "#generated/common/PageInput"
import type { PlatformBulkPayoutFilterInput } from "#generated/platform/bulkPayout/PlatformBulkPayoutFilterInput"

export type GetPlatformBulkPayoutsBody = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformBulkPayoutFilterInput
}
