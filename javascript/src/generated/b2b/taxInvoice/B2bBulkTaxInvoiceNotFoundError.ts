/** 일괄 세금계산서가 존재하지 않은 경우 */
export type B2bBulkTaxInvoiceNotFoundError = {
	type: "B2B_BULK_TAX_INVOICE_NOT_FOUND"
	message?: string
}
