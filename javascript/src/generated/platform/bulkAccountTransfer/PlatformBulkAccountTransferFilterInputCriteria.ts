import type { DateTimeRange } from "./../../common/DateTimeRange"
export type PlatformBulkAccountTransferFilterInputCriteria = {
	/** 생성 일시 범위 */
	timestampRange?: DateTimeRange
	/** 상태 업데이트 일시 범위 */
	statusUpdatedTimestampRange?: DateTimeRange
	/** 일괄 이체 아이디 */
	bulkAccountTransferId?: string
}
