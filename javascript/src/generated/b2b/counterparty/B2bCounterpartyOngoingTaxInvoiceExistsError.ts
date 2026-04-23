/** 진행 중인 세금계산서가 존재하여 거래처를 삭제할 수 없는 경우 */
export type B2bCounterpartyOngoingTaxInvoiceExistsError = {
	type: "B2B_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS"
	message?: string
}
