import type { B2bTaxInvoice } from "#generated/b2b/TaxInvoice/B2bTaxInvoice"

/** 세금계산서 역발행 즉시 요청 응답 */
export type RequestB2bTaxInvoiceReverseIssuanceResponse = {
	taxInvoice: B2bTaxInvoice
}
