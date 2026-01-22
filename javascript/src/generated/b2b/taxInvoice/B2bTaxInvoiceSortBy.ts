/** 세금계산서 정렬 기준 */
export type B2bTaxInvoiceSortBy =
	/** 작성일자 */
	| "WRITE_DATE"
	/** 발행마감일 */
	| "ISSUANCE_DUE_DATE"
	/** 합계금액 */
	| "TOTAL_AMOUNT"
	/** 공급가액 */
	| "TOTAL_SUPPLY_AMOUNT"
	/** 세액 */
	| "TOTAL_TAX_AMOUNT"
	/** 발행요청일시 */
	| "REQUESTED_AT"
	/** 발행완료일시 */
	| "ISSUED_AT"
	/** 국세청전송일시 */
	| "NTS_SENT_AT"
	/** 상태 업데이트 일시 */
	| "STATUS_UPDATED_AT"
	| string & {}
