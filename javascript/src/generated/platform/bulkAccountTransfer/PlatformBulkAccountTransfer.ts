import type { PlatformBulkAccountTransferStats } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransferStats"
import type { PlatformBulkAccountTransferStatus } from "./../../platform/bulkAccountTransfer/PlatformBulkAccountTransferStatus"
export type PlatformBulkAccountTransfer = {
	/** 일괄 이체 고유 아이디 */
	id: string
	graphqlId: string
	creatorId: string
	/** 출금 계좌 아이디 */
	bankAccountId: string
	bankAccountGraphqlId: string
	/** (int64) */
	totalAmount: number
	status: PlatformBulkAccountTransferStatus
	stats: PlatformBulkAccountTransferStats
	/** (RFC 3339 date-time) */
	statusUpdatedAt: string
	/** (RFC 3339 date-time) */
	createdAt: string
	/** (RFC 3339 date-time) */
	updatedAt: string
	/** (RFC 3339 date-time) */
	scheduledAt?: string
}
