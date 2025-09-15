import type { B2bTaxInvoice } from "./../../b2b/taxInvoice/B2bTaxInvoice"
/** 세금계산서 역발행 요청 취소 응답 */
export type CancelB2bTaxInvoiceRequestResponse = {
	taxInvoice: B2bTaxInvoice
}
