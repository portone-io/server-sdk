import type { CursorPageInfo } from "#generated/platform/CursorPageInfo"
import type { PaymentReconciliationSettlementSummaryWithCursor } from "#generated/platform/PaymentReconciliationSettlementSummaryWithCursor"

export type GetPaymentReconciliationSettlementSummariesResponse = {
	items: PaymentReconciliationSettlementSummaryWithCursor[]
	pageInfo: CursorPageInfo
}
