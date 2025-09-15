export type B2bTaxInvoiceStatus =
	/** 임시저장 */
	| "DRAFTED"
	/** 임시저장 대기 */
	| "DRAFT_PENDING"
	/** 임시저장 실패 */
	| "DRAFT_FAILED"
	/** 역발행 요청 완료 (전자 서명 요청됨) */
	| "REQUESTED"
	/** 역발행 요청 대기 */
	| "REQUEST_PENDING"
	/** 역발행 요청 실패 */
	| "REQUEST_FAILED"
	/** 공급받는자에 의한 발행취소 */
	| "REQUEST_CANCELLED"
	/** 발행완료 */
	| "ISSUED"
	/** 발행 대기 */
	| "ISSUE_PENDING"
	/** 발행 실패 */
	| "ISSUE_FAILED"
	/** 전송전 */
	| "BEFORE_SENDING"
	/** 전송대기 */
	| "WAITING_SENDING"
	/** 전송중 */
	| "SENDING"
	/** 전송완료 */
	| "SENDING_COMPLETED"
	/** 전송실패 */
	| "SENDING_FAILED"
	/** 공급자의 발행거부 */
	| "REQUEST_REFUSED"
	/** 공급자에 의한 발행 취소 */
	| "ISSUANCE_CANCELLED"
	| string & {}
