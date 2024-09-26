import type { B2bTaxInvoiceDocumentKeyType } from "#generated/b2b/B2bTaxInvoiceDocumentKeyType"

/** 세금계산서 발행 정보 */
export type IssueB2bTaxInvoiceRequestBody = {
	/** 사업자등록번호 */
	brn: string
	/** 세금계산서 문서 번호 */
	documentKey: string
	/**
	 * 문서 번호 유형
	 *
	 * 기본 값은 RECIPIENT이며 SUPPLIER, RECIPIENT을 지원합니다.
	 */
	documentKeyType?: B2bTaxInvoiceDocumentKeyType
	/** 메모 */
	memo?: string
	/** 이메일 제목 */
	emailSubject?: string
}
