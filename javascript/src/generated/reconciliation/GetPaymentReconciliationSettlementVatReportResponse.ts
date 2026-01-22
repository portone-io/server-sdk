import type { PaymentReconciliationVatReportItem } from "./../reconciliation/PaymentReconciliationVatReportItem"
import type { PaymentReconciliationVatReportSummary } from "./../reconciliation/PaymentReconciliationVatReportSummary"
import type { ReconciliationPgSpecifier } from "./../reconciliation/ReconciliationPgSpecifier"
export type GetPaymentReconciliationSettlementVatReportResponse = {
	/** 부가세 내역 항목 리스트 */
	items?: PaymentReconciliationVatReportItem[]
	/** 부가세 내역 요약 */
	summary: PaymentReconciliationVatReportSummary
	/** PG사 식별자 리스트 */
	pgSpecifiers?: ReconciliationPgSpecifier[]
}
