import type { B2bTaxInvoiceKeyType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceKeyType"
import type { B2bTaxInvoiceModificationType } from "#generated/b2b/TaxInvoice/B2bTaxInvoiceModificationType"

/** 수정 세금계산서 생성 입력 정보 */
export type B2bTaxInvoiceModificationCreateBody = {
	/** 수정 사유 */
	type: B2bTaxInvoiceModificationType
	/**
	 * 사업자등록번호
	 *
	 * taxInvoiceKeyType이 TAX_INVOICE_ID가 아닌 경우 필수 값입니다.
	 */
	brn?: string
	/** 세금계산서 문서 번호 */
	taxInvoiceKey: string
	/**
	 * 문서 번호 유형
	 *
	 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
	 */
	taxInvoiceKeyType?: B2bTaxInvoiceKeyType
}
