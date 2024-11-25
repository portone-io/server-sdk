import type { Bank } from "./../../common/Bank"
import type { Currency } from "./../../common/Currency"
import type { PlatformPayoutFilterInputCriteria } from "./../../platform/payout/PlatformPayoutFilterInputCriteria"
import type { PlatformPayoutStatus } from "./../../platform/payout/PlatformPayoutStatus"
export type PlatformPayoutFilterInput = {
	statuses?: PlatformPayoutStatus[]
	partnerIds?: string[]
	criteria: PlatformPayoutFilterInputCriteria
	/** 은행 */
	payoutAccountBanks?: Bank[]
	partnerTags?: string[]
	/** 통화 단위 */
	payoutCurrencies?: Currency[]
}
