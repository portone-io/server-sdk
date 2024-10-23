/** 세금계산서가 임시저장 상태가 아닌 경우 */
export type B2bTaxInvoiceNotDraftedStatusError = {
	type: "B2B_TAX_INVOICE_NOT_DRAFTED_STATUS"
	message?: string
}
