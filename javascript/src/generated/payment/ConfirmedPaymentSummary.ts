/** 결제 수동 승인 완료된 결제 건 요약 정보 */
export type ConfirmedPaymentSummary = {
	/** PG사 결제 아이디 */
	pgTxId: string
	/**
	 * 결제 완료 시점
	 * (RFC 3339 date-time)
	 */
	paidAt: string
}
