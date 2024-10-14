/** 결제 예약 건 취소 성공 응답 */
export type RevokePaymentSchedulesResponse = {
	/** 취소 완료된 결제 예약 건 아이디 목록 */
	revokedScheduleIds: string[]
	/**
	 * 결제 예약 건 취소 완료 시점
	 * (RFC 3339 date-time)
	 */
	revokedAt?: string
}
