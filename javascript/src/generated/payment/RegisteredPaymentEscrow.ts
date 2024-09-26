/** 배송 정보 등록 완료 */
export type RegisteredPaymentEscrow = {
	/** 에스크로 상태 */
	status: "REGISTERED"
	/** 택배사 */
	company: string
	/** 송장번호 */
	invoiceNumber: string
	/**
	 * 발송 일시
	 * (RFC 3339 date-time)
	 */
	sentAt?: string
	/**
	 * 배송등록 처리 일자
	 * (RFC 3339 date-time)
	 */
	appliedAt?: string
}
