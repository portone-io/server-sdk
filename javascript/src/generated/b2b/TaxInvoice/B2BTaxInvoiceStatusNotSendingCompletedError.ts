/** 원본 세금계산서가 전송완료 상태가 아닌 경우 */
export type B2BTaxInvoiceStatusNotSendingCompletedError = {
	type: "B2B_TAX_INVOICE_STATUS_NOT_SENDING_COMPLETED"
	message?: string
}
