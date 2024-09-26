import type { DateRange } from "#generated/platform/DateRange"
import type { PaymentReconciliationSettlementSummaryColumn } from "#generated/platform/PaymentReconciliationSettlementSummaryColumn"
import type { PaymentReconciliationSettlementSummaryExcelFileFilterInput } from "#generated/platform/PaymentReconciliationSettlementSummaryExcelFileFilterInput"

export type GetPaymentReconciliationSettlementSummaryExcelFileBody = {
	/** 정산일 범위 */
	dateRange: DateRange
	filter?: PaymentReconciliationSettlementSummaryExcelFileFilterInput
	/** 액셀파일 요청시 선택 필드 */
	columns: PaymentReconciliationSettlementSummaryColumn[]
}
