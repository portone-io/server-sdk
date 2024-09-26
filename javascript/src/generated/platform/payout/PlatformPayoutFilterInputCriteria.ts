import type { DateTimeRange } from "#generated/common/DateTimeRange"

/** 검색 기준 입력 정보 */
export type PlatformPayoutFilterInputCriteria = {
	timestampRange?: DateTimeRange
	payoutId?: string
	bulkPayoutId?: string
}
