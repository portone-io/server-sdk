import type { DateRange } from "#generated/platform/DateRange"

/**
 * 거래 대사 날짜 범위 조회 필드
 *
 * 필드 중 하나만 적용됩니다.
 */
export type ReconciliationDateConditionInput = {
	/** 정산일 범위 */
	settlementDateRange?: DateRange
	/** 결제일 범위 */
	transactionDateRange?: DateRange
}
