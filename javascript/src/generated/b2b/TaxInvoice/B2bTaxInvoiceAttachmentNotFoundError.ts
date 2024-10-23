/** 세금계산서의 첨부파일을 찾을 수 없는 경우 */
export type B2bTaxInvoiceAttachmentNotFoundError = {
	type: "B2B_TAX_INVOICE_ATTACHMENT_NOT_FOUND"
	message?: string
}
