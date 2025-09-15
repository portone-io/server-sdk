import type { B2bTaxInvoice } from "./../../b2b/taxInvoice/B2bTaxInvoice"
/** 세금계산서 즉시 정발행 응답 */
export type IssueB2bTaxInvoiceImmediatelyResponse = {
	taxInvoice: B2bTaxInvoice
}
