/** 에스크로 배송 정보 등록 성공 응답 */
export type ApplyEscrowLogisticsResponse = {
	/** 송장 번호 */
	invoiceNumber: string
	/**
	 * 발송 시점
	 * (RFC 3339 date-time)
	 */
	sentAt: string
	/**
	 * 에스크로 정보 등록 시점
	 * (RFC 3339 date-time)
	 */
	appliedAt: string
}
