/** 세금계산서에 공급 받는자 문서 번호가 이미 사용 중인 경우 */
export type B2bTaxInvoiceRecipientDocumentKeyAlreadyUsedError = {
	type: "B2B_TAX_INVOICE_RECIPIENT_DOCUMENT_KEY_ALREADY_USED"
	message?: string
}
