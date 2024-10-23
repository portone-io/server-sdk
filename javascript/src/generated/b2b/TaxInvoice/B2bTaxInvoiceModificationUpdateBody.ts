import type { B2bTaxInvoiceModificationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceModificationType"

/** 임시 저장된 수정 세금계산서 업데이트 입력 정보 */
export type B2bTaxInvoiceModificationUpdateBody = {
	/** 수정 사유 */
	type: B2bTaxInvoiceModificationType
}
