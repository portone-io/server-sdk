import type { CursorPageInfo } from "#generated/platform/CursorPageInfo"
import type { PaymentReconciliationTransactionSummaryWithCursor } from "#generated/platform/PaymentReconciliationTransactionSummaryWithCursor"

export type GetPaymentReconciliationTransactionSummariesResponse = {
	items: PaymentReconciliationTransactionSummaryWithCursor[]
	pageInfo: CursorPageInfo
}
