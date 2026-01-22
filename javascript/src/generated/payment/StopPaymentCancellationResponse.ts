/** 결제 취소 요청 취소 성공 응답 */
export type StopPaymentCancellationResponse = {
	/**
	 * 결제 취소 요청 취소 완료 시각
	 * (RFC 3339 date-time)
	 */
	stoppedAt: string
}
