/** 세금계산서가 존재하지 않은 경우 */
export type B2bTaxInvoiceNotFoundError = {
	type: "B2B_TAX_INVOICE_NOT_FOUND"
	message?: string
}
