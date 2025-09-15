/** 그룹 생성 방식 */
export type B2bBulkTaxInvoiceSourceType =
	/** 엑셀 업로드 */
	| "SHEET"
	/** 지급 데이터 기반 생성 */
	| "PLATFORM"
	| string & {}
