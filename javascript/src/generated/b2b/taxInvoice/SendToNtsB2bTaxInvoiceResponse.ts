import type { B2bTaxInvoice } from "./../../b2b/taxInvoice/B2bTaxInvoice"
/** 세금계산서 국세청 즉시 전송 응답 */
export type SendToNtsB2bTaxInvoiceResponse = {
	taxInvoice: B2bTaxInvoice
}
