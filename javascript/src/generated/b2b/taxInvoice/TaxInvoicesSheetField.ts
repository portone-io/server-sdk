/** 다운로드 할 시트 컬럼 */
export type TaxInvoicesSheetField =
	/** 상태 */
	| "STATUS"
	/** 취소사유 */
	| "CANCEL_REASON"
	/** 발행유형 */
	| "ISSUANCE_TYPE"
	/** 문서형태 */
	| "DOCUMENT_MODIFICATION_TYPE"
	/** 지연발행 */
	| "IS_DELAYED"
	/** 작성일자 */
	| "WRITE_DATE"
	/** 발행마감일 */
	| "ISSUANCE_DUE_DATE"
	/** 과세형태 */
	| "TAXATION_TYPE"
	/** 영수/청구 */
	| "PURPOSE_TYPE"
	/** 거래처 회사명 */
	| "PARTNER_NAME"
	/** 거래처 사업자등록번호 */
	| "PARTNER_BRN"
	/** 합계금액 */
	| "TOTAL_AMOUNT"
	/** 공급가액 */
	| "TOTAL_SUPPLY_AMOUNT"
	/** 세액 */
	| "TOTAL_TAX_AMOUNT"
	/** 관리용 메모 */
	| "MEMO"
	/** 발행요청일시 */
	| "REQUESTED_AT"
	/** 발행완료일시 */
	| "ISSUED_AT"
	/** 국세청 전송일시 */
	| "NTS_SENT_AT"
	/** 상태 업데이트 일시 */
	| "STATUS_UPDATED_AT"
	/** 일괄 세금계산서 아이디 */
	| "BULK_TAX_INVOICE_ID"
	/** 세금계산서 아이디 */
	| "PLAIN_ID"
	/** 공급자 문서번호 */
	| "SUPPLIER_DOCUMENT_KEY"
	/** 공급받는자 문서번호 */
	| "RECIPIENT_DOCUMENT_KEY"
	/** 지급 아이디 */
	| "PAYOUT_ID"
	/** 품목 */
	| "ITEMS"
	| string & {}
