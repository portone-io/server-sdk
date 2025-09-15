import type { B2bTaxInvoice } from "./../../b2b/taxInvoice/B2bTaxInvoice"
/** 세금계산서 역발행 요청 응답 */
export type RequestB2bTaxInvoiceResponse = {
	taxInvoice: B2bTaxInvoice
}
