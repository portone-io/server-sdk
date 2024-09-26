import type { SortOrder } from "#generated/common/SortOrder"

/**
 * 거래대사 거래 건 별 조회 정렬 조건
 *
 * 필드중 하나만 명시하여야 합니다
 */
export type PaymentReconciliationOrderInput = {
	/** 정산일 기준 정렬 */
	settlementDate?: SortOrder
	/** 결제일 기준 정렬 */
	transactionDate?: SortOrder
	/** 결제 금액 기준 정렬 */
	transactionAmount?: SortOrder
	/** 거래이상 금액 기준 정렬 */
	anomalyAmount?: SortOrder
	/** 정산 금액 기준 정렬 */
	settlementAmount?: SortOrder
}
