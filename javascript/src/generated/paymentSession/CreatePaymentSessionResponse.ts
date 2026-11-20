/** 결제 세션 생성 성공 응답 */
export type CreatePaymentSessionResponse = {
	/** 세션 아이디 */
	sessionId: string
	/** 호스티드 체크아웃 페이지 URL */
	url: string
	/**
	 * 만료 시각
	 * (RFC 3339 date-time)
	 */
	expiresAt: string
}
