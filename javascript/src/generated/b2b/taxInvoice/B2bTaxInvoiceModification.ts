import type { B2bTaxInvoiceModificationType } from "./../../b2b/taxInvoice/B2bTaxInvoiceModificationType"
/** 세금 계산서 수정 */
export type B2bTaxInvoiceModification = {
	/** 수정 사유 */
	type: B2bTaxInvoiceModificationType
	/** 수정 대상 원본 세금계산서 국세청 승인 번호 */
	originalNtsApprovalNumber: string
	/** 원본 세금계산서 아이디 */
	originalTaxInvoiceId: string
	/** 최초 원본 세금계산서 아이디 */
	rootTaxInvoiceId: string
}
