import type { DateRange } from "#generated/platform/DateRange"
import type { PaymentReconciliationTransactionSummaryColumn } from "#generated/platform/PaymentReconciliationTransactionSummaryColumn"
import type { PaymentReconciliationTransactionSummaryExcelFilterInput } from "#generated/platform/PaymentReconciliationTransactionSummaryExcelFilterInput"

export type GetPaymentReconciliationTransactionSummaryExcelFileBody = {
	/** 거래일 범위 */
	dateRange: DateRange
	filter?: PaymentReconciliationTransactionSummaryExcelFilterInput
	/** 액셀파일 요청시 선택 필드 */
	columns: PaymentReconciliationTransactionSummaryColumn[]
}
