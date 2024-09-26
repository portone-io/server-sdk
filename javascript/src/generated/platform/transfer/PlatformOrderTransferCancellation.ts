/** 주문 취소 정보 */
export type PlatformOrderTransferCancellation = {
	/** 주문 취소 아이디 */
	id: string
	/**
	 * 취소 일시
	 * (RFC 3339 date-time)
	 */
	cancelledAt: string
}
