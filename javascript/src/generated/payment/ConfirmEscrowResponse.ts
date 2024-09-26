/** 에스크로 구매 확정 성공 응답 */
export type ConfirmEscrowResponse = {
	/**
	 * 에스크로 구매 확정 시점
	 * (RFC 3339 date-time)
	 */
	completedAt: string
}
