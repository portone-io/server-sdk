/** 웹훅 요청 정보 */
export type PaymentWebhookRequest = {
	/** 요청 헤더 */
	header?: string
	/** 요청 본문 */
	body: string
	/**
	 * 요청 시점
	 * (RFC 3339 date-time)
	 */
	requestedAt?: string
}
