/** 정산 내역서 발송 상태 */
export type PlatformPayoutSettlementStatementStatus =
	/** 미발송 */
	| "UNSENT"
	/** 발송 성공 */
	| "SENT"
	/** 발송 실패 */
	| "SEND_FAILED"
	/** 발송 대기 */
	| "SEND_PREPARED"
	| string & {}
