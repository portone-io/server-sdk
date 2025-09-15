import type { B2bTaxInvoiceInput } from "./../../b2b/taxInvoice/B2bTaxInvoiceInput"
import type { B2bTaxInvoiceModificationCreateBody } from "./../../b2b/taxInvoice/B2bTaxInvoiceModificationCreateBody"
/** 세금계산서 임시 저장 정보 */
export type DraftB2bTaxInvoiceBody = {
	/** 세금계산서 생성 요청 정보 */
	taxInvoice: B2bTaxInvoiceInput
	/** 수정 세금계산서 입력 정보 */
	modification?: B2bTaxInvoiceModificationCreateBody
	/** 메모 */
	memo?: string
}
