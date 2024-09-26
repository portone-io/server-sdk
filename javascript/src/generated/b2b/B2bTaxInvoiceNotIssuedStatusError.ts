/** 세금계산서가 발행된(ISSUED) 상태가 아닌 경우 */
export type B2bTaxInvoiceNotIssuedStatusError = {
	type: "B2B_TAX_INVOICE_NOT_ISSUED_STATUS"
	message?: string
}
