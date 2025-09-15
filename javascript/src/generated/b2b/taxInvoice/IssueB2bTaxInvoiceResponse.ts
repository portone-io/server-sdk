import type { B2bTaxInvoice } from "./../../b2b/taxInvoice/B2bTaxInvoice"
/** 세금계산서 발행 승인 응답 */
export type IssueB2bTaxInvoiceResponse = {
	taxInvoice: B2bTaxInvoice
}
