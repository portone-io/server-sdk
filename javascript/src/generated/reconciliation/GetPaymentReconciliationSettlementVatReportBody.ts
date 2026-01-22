import type { DateRange } from "./../common/DateRange"
import type { PaymentReconciliationSettlementSummaryFilterInput } from "./../reconciliation/PaymentReconciliationSettlementSummaryFilterInput"
export type GetPaymentReconciliationSettlementVatReportBody = {
	/** 정산일 범위 */
	dateRange: DateRange
	filter?: PaymentReconciliationSettlementSummaryFilterInput
}
