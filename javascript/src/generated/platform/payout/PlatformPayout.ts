import type { Currency } from "./../../common/Currency"
import type { PlatformPartner } from "./../../platform/PlatformPartner"
import type { PlatformPayoutAccount } from "./../../platform/payout/PlatformPayoutAccount"
import type { PlatformPayoutMethod } from "./../../platform/PlatformPayoutMethod"
import type { PlatformPayoutStatus } from "./../../platform/payout/PlatformPayoutStatus"
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
