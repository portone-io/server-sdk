import type { DateTimeRange } from "./../../common/DateTimeRange"
/** 검색 기준 입력 정보 */
export type PlatformPayoutFilterInputCriteria = {
	/** 시간 범위 */
	timestampRange?: DateTimeRange
	/** 지급 아이디 */
	payoutId?: string
	/** 일괄 지급 아이디 */
	bulkPayoutId?: string
}
