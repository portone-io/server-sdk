/** 세금계산서 문서 수정 발행 유형 */
export type B2bTaxInvoiceDocumentModificationType =
	/** 정상발행 */
	| "NORMAL"
	/** 수정발행 */
	| "MODIFICATION"
	| string & {}
