import type { Currency } from "#generated/common/Currency"
import type { PlatformPartner } from "#generated/platform/PlatformPartner"
import type { PlatformPayoutAccount } from "#generated/platform/payout/PlatformPayoutAccount"
import type { PlatformPayoutMethod } from "#generated/platform/PlatformPayoutMethod"
import type { PlatformPayoutStatus } from "#generated/platform/payout/PlatformPayoutStatus"

export type PlatformPayout = {
	/** 지급 고유 아이디 */
	id: string
	graphqlId: string
	method: PlatformPayoutMethod
	status: PlatformPayoutStatus
	/** (RFC 3339 date-time) */
	statusUpdatedAt: string
	memo?: string
	partner: PlatformPartner
	account: PlatformPayoutAccount
	currency: Currency
	/** (int64) */
	amount: number
	/** (int64) */
	settlementAmount: number
	/** (int64) */
	incomeTaxAmount: number
	/** (int64) */
	localIncomeTaxAmount: number
	withdrawalMemo?: string
	depositMemo?: string
	/** (RFC 3339 date-time) */
	createdAt: string
	/** (RFC 3339 date-time) */
	scheduledAt?: string
}
