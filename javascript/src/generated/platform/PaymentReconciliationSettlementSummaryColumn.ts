/** 거래대사 정산 요약 내역 엑셀파일 필드 */
export type PaymentReconciliationSettlementSummaryColumn =
	/** 취소금액 필드 */
	| "CANCEL_AMOUNT"
	/** 취소건수 필드 */
	| "CANCEL_COUNT"
	/** PG 수수료 필드 */
	| "SETTLEMENT_FEE"
	/** 거래금액 필드 */
	| "TRANSACTION_AMOUNT"
	/** 정산일 필드 */
	| "SETTLEMENT_DATE"
	/** 포트원 상점 아이디 필드 */
	| "STORE_ID"
	/** 정산금액 필드 */
	| "SETTLEMENT_AMOUNT"
	/** 정산건수 필드 */
	| "SETTLEMENT_COUNT"
	/** 대사용 PG사 가맹점 식별자 필드 */
	| "RECONCILIATION_PG_SPECIFIER"
	/** PG 수수료 부가세 필드 */
	| "SETTLEMENT_FEE_VAT"
