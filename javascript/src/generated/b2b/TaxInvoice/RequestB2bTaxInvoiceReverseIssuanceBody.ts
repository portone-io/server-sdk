import type { B2bTaxInvoiceInput } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceInput"
import type { B2bTaxInvoiceModificationCreateBody } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceModificationCreateBody"

/** 세금계산서 역발행 즉시 요청 정보 */
export type RequestB2bTaxInvoiceReverseIssuanceBody = {
	/** 세금계산서 생성 요청 정보 */
	taxInvoice: B2bTaxInvoiceInput
	/** 메모 */
	memo?: string
	/** 수정 세금계산서 입력 정보 */
	modification?: B2bTaxInvoiceModificationCreateBody
}
