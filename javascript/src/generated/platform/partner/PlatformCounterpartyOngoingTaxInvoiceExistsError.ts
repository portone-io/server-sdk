/** 연동된 거래처에 진행 중인 세금계산서가 있는 경우 */
export type PlatformCounterpartyOngoingTaxInvoiceExistsError = {
	type: "PLATFORM_COUNTERPARTY_ONGOING_TAX_INVOICE_EXISTS"
	message?: string
}
