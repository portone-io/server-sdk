import type { DateRange } from "#generated/platform/DateRange"

export type GetPaymentReconciliationSettlementSummariesBody = {
	/** 정산일 범위 */
	dateRange: DateRange
	/**
	 * 조회할 건 수
	 * (int32)
	 */
	size: number
	/** 이전 페이지의 마지막 커서 */
	after?: string
}
