import type { CursorPageInfo } from "#generated/platform/CursorPageInfo"
import type { PaymentReconciliationWithCursor } from "#generated/platform/PaymentReconciliationWithCursor"

export type GetPaymentReconciliationsResponse = {
	items: PaymentReconciliationWithCursor[]
	pageInfo: CursorPageInfo
}
