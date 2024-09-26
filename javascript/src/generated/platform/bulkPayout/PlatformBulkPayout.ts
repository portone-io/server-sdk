import type { PlatformBulkPayoutStats } from "#generated/platform/bulkPayout/PlatformBulkPayoutStats"
import type { PlatformBulkPayoutStatus } from "#generated/platform/bulkPayout/PlatformBulkPayoutStatus"
import type { PlatformPayoutMethod } from "#generated/platform/PlatformPayoutMethod"

export type PlatformBulkPayout = {
	/** 일괄 지급 고유 아이디 */
	id: string
	graphqlId: string
	name: string
	creatorId: string
	method: PlatformPayoutMethod
	arePayoutsGenerated: boolean
	/** (int64) */
	totalPayoutAmount: number
	status: PlatformBulkPayoutStatus
	payoutStats: PlatformBulkPayoutStats
	/** (RFC 3339 date-time) */
	statusUpdatedAt: string
	/** (RFC 3339 date-time) */
	createdAt: string
	/** (RFC 3339 date-time) */
	updatedAt: string
}
