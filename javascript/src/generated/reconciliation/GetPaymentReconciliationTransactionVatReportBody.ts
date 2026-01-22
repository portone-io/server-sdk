import type { DateRange } from "./../common/DateRange"
import type { PaymentReconciliationTransactionSummaryFilterInput } from "./../reconciliation/PaymentReconciliationTransactionSummaryFilterInput"
export type GetPaymentReconciliationTransactionVatReportBody = {
	/** 거래일 범위 */
	dateRange: DateRange
	filter?: PaymentReconciliationTransactionSummaryFilterInput
}
