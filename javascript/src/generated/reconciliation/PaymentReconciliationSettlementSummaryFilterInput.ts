import type { ReconciliationPgSpecifier } from "./../reconciliation/ReconciliationPgSpecifier"
/** 거래대사 정산 요약 내역 필터 */
export type PaymentReconciliationSettlementSummaryFilterInput = {
	/** PG사 가맹점 식별자 필터 */
	pgSpecifiers?: ReconciliationPgSpecifier[]
	/** 하위 상점 아이디 필터 */
	storeIds?: string[]
}
