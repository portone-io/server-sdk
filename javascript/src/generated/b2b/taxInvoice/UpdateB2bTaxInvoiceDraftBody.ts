import type { B2bTaxInvoiceInput } from "./../../b2b/taxInvoice/B2bTaxInvoiceInput"
import type { B2bTaxInvoiceKeyType } from "./../../b2b/taxInvoice/B2bTaxInvoiceKeyType"
/** 세금계산서 임시저장 수정 정보 */
export type UpdateB2bTaxInvoiceDraftBody = {
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
	/** 세금계산서 임시저장 수정 정보 */
	taxInvoice: B2bTaxInvoiceInput
	/** 메모 */
	memo?: string
}
