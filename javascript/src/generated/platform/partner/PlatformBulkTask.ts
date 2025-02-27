import type { PlatformBulkTaskProgressStats } from "./../../platform/partner/PlatformBulkTaskProgressStats"
import type { PlatformBulkTaskStatus } from "./../../platform/partner/PlatformBulkTaskStatus"
import type { PlatformBulkTaskType } from "./../../platform/partner/PlatformBulkTaskType"
export type PlatformBulkTask = {
	id: string
	graphqlId: string
	status: PlatformBulkTaskStatus
	type: PlatformBulkTaskType
	progressStats: PlatformBulkTaskProgressStats
	isForTest: boolean
	/** (RFC 3339 date-time) */
	statusUpdatedAt: string
	/** (RFC 3339 date-time) */
	createdAt: string
	/** (RFC 3339 date-time) */
	updatedAt: string
}
