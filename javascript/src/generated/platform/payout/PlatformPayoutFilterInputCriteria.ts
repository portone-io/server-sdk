import type { DateTimeRange } from "./../../common/DateTimeRange"
/** 검색 기준 입력 정보 */
export type PlatformPayoutFilterInputCriteria = {
	/** 생성 일시 범위 */
	timestampRange?: DateTimeRange
	/** 상태 업데이트 일시 범위 */
	statusUpdatedTimestampRange?: DateTimeRange
	/** 지급 예정 일시 범위 */
	scheduledTimestampRange?: DateTimeRange
	/** 정산 내역서 발송 일시 범위 */
	settlementStatementIssuedTimestampRange?: DateTimeRange
	/** 지급 아이디 */
	payoutId?: string
	/** 일괄 지급 아이디 */
	bulkPayoutId?: string
	/** 세금계산서 아이디 */
	taxInvoiceId?: string
	/** 정산 내역서 아이디 */
	settlementStatementId?: string
}
