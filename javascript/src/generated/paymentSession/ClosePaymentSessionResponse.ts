/** 결제 세션 종료 성공 응답 */
export type ClosePaymentSessionResponse = {
	/**
	 * 결제 세션 종료 시각
	 * (RFC 3339 date-time)
	 */
	closedAt: string
}
