/** 진행 중인 세금계산서가 존재하는 경우 */
export type PlatformOngoingTaxInvoiceExistsError = {
	type: "PLATFORM_ONGOING_TAX_INVOICE_EXISTS"
	message?: string
}
