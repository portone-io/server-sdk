import type { PlatformBulkPayoutStats } from "./../../platform/bulkPayout/PlatformBulkPayoutStats"
import type { PlatformBulkPayoutStatus } from "./../../platform/bulkPayout/PlatformBulkPayoutStatus"
import type { PlatformPayoutMethod } from "./../../platform/PlatformPayoutMethod"
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
	/** (RFC 3339 date-time) */
	scheduledAt?: string
}
