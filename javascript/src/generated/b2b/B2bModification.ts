import type { B2bTaxInvoiceModificationType } from "#generated/b2b/B2bTaxInvoiceModificationType"

/** 세금 계산서 수정 */
export type B2bModification = {
	/** 수정 사유 */
	type: B2bTaxInvoiceModificationType
	/** 수정 대상 원본 세금계산서 국세청 승인 번호 */
	originalNtsApproveNumber: string
}
