/** 거래대사 정산 요약 내역 엑셀파일 필드 */
export type PaymentReconciliationTransactionSummaryColumn =
	/** 취소 금액 필드 */
	| "CANCEL_AMOUNT"
	/** 거래 건수 필드 */
	| "TRANSACTION_COUNT"
	/** 대사용 PG사 가맹점 식별자 필드 */
	| "RECONCILIATION_PG_SPECIFIER"
	/** 거래일 필드 */
	| "TRANSACTION_DATE"
	/** 취소 건수 필드 */
	| "CANCEL_COUNT"
	/** 거래이상 금액 필드 */
	| "ANOMALY_AMOUNT"
	/** 대사상태 필드 */
	| "RECONCILIATION_STATUS"
	/** 거래 금액 필드 */
	| "TRANSACTION_AMOUNT"
	/** 포트원 상점 아이디 필드 */
	| "STORE_ID"
	/** 거래이상 건수 필드 */
	| "ANOMALY_COUNT"
