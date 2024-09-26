import type { PageInput } from "#generated/common/PageInput"
import type { PlatformPayoutFilterInput } from "#generated/platform/payout/PlatformPayoutFilterInput"

export type GetPlatformPayoutsBody = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformPayoutFilterInput
}
