import type { B2bTaxInvoiceInput } from "#generated/b2b/B2bTaxInvoiceInput"

/** 세금계산서 역발행 요청 정보 */
export type RequestB2bTaxInvoiceReverseIssuanceRequestBody = {
	/** 세금계산서 생성 요청 정보 */
	taxInvoice: B2bTaxInvoiceInput
	/** 메모 */
	memo?: string
}
