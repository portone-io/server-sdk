import type { B2bTaxInvoiceInput } from "#generated/b2b/B2bTaxInvoiceInput"

/** 세금계산서 임시 저장 정보 */
export type RequestB2bTaxInvoiceRegisterBody = {
	/** 세금계산서 생성 요청 정보 */
	taxInvoice: B2bTaxInvoiceInput
}
