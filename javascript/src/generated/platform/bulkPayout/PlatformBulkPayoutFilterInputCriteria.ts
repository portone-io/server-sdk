import type { DateTimeRange } from "./../../common/DateTimeRange"
export type PlatformBulkPayoutFilterInputCriteria = {
	/** 생성 일시 범위 */
	timestampRange?: DateTimeRange
	/** 상태 업데이트 일시 범위 */
	statusUpdatedTimestampRange?: DateTimeRange
	/** 일괄 지급 아이디 */
	bulkPayoutId?: string
}
