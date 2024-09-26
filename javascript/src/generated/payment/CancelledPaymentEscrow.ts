/** 거래 취소 */
export type CancelledPaymentEscrow = {
	/** 에스크로 상태 */
	status: "CANCELLED"
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
