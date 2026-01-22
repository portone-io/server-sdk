import type { PaymentReconciliationStatus } from "./../reconciliation/PaymentReconciliationStatus"
import type { ReconciliationPgSpecifier } from "./../reconciliation/ReconciliationPgSpecifier"
/** 거래대사 거래내역 필터 */
export type PaymentReconciliationTransactionSummaryFilterInput = {
	/** 대사 상태 필터 */
	reconciliationStatuses?: PaymentReconciliationStatus[]
	/** 대사용 PG사 가맹점 식별자 필터 */
	pgSpecifiers?: ReconciliationPgSpecifier[]
	/** 하위 상점 아이디 필터 */
	storeIds?: string[]
}
