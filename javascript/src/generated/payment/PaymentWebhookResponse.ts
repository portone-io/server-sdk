/** 웹훅 응답 정보 */
export type PaymentWebhookResponse = {
	/** 응답 HTTP 코드 */
	code: string
	/** 응답 헤더 */
	header: string
	/** 응답 본문 */
	body: string
	/**
	 * 응답 시점
	 * (RFC 3339 date-time)
	 */
	respondedAt: string
}
