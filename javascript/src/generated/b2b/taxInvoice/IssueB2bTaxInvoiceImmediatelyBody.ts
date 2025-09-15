import type { B2bTaxInvoiceInput } from "./../../b2b/taxInvoice/B2bTaxInvoiceInput"
import type { B2bTaxInvoiceModificationCreateBody } from "./../../b2b/taxInvoice/B2bTaxInvoiceModificationCreateBody"
/** 세금계산서 즉시 정발행 요청 정보 */
export type IssueB2bTaxInvoiceImmediatelyBody = {
	/** 세금계산서 생성 요청 정보 */
	taxInvoice: B2bTaxInvoiceInput
	/** 메모 */
	memo?: string
	/** 수정 세금계산서 입력 정보 */
	modification?: B2bTaxInvoiceModificationCreateBody
}
