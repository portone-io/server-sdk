/** 현금영수증이 존재하지 않는 경우 */
export type CashReceiptNotFoundError = {
	type: "CASH_RECEIPT_NOT_FOUND"
	message?: string
}
