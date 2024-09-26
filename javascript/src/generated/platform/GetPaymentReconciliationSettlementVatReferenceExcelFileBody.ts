import type { DateRange } from "#generated/platform/DateRange"
import type { PaymentReconciliationSettlementSummaryFilterInput } from "#generated/platform/PaymentReconciliationSettlementSummaryFilterInput"

export type GetPaymentReconciliationSettlementVatReferenceExcelFileBody = {
	/** 정산일 범위 */
	dateRange: DateRange
	filter?: PaymentReconciliationSettlementSummaryFilterInput
}
