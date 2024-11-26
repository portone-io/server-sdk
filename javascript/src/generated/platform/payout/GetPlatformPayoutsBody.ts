import type { PageInput } from "./../../common/PageInput"
import type { PlatformPayoutFilterInput } from "./../../platform/payout/PlatformPayoutFilterInput"
export type GetPlatformPayoutsBody = {
	isForTest?: boolean
	page?: PageInput
	filter?: PlatformPayoutFilterInput
}
