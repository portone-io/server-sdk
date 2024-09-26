import type { B2bTaxInvoiceDocumentKeyType } from "#generated/b2b/B2bTaxInvoiceDocumentKeyType"

/** 세금계산서 파일 첨부 정보 */
export type AttachB2bTaxInvoiceFileBody = {
	/**
	 * 사업자등록번호
	 *
	 * `-` 없이 숫자 10자리로 구성됩니다.
	 */
	brn: string
	/** 세금계산서 문서 번호 */
	documentKey: string
	/**
	 * 문서 번호 유형
	 *
	 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
	 */
	documentKeyType?: B2bTaxInvoiceDocumentKeyType
	/** 파일 아이디 */
	fileId: string
}
