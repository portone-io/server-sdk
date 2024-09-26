/** 현금영수증이 이미 발급된 경우 */
export type CashReceiptAlreadyIssuedError = {
	type: "CASH_RECEIPT_ALREADY_ISSUED"
	message?: string
}
