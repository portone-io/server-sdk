import type { Bank } from "#generated/common/Bank"
import type { Currency } from "#generated/common/Currency"
import type { PlatformPayoutFilterInputCriteria } from "#generated/platform/payout/PlatformPayoutFilterInputCriteria"
import type { PlatformPayoutStatus } from "#generated/platform/payout/PlatformPayoutStatus"

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
