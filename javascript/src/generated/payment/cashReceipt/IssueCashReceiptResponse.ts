import type { CashReceiptSummary } from "#generated/payment/cashReceipt/CashReceiptSummary"

/** 현금 영수증 발급 성공 응답 */
export type IssueCashReceiptResponse = {
	cashReceipt: CashReceiptSummary
}
