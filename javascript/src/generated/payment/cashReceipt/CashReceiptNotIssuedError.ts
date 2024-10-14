/** 현금영수증이 발급되지 않은 경우 */
export type CashReceiptNotIssuedError = {
	type: "CASH_RECEIPT_NOT_ISSUED"
	message?: string
}
