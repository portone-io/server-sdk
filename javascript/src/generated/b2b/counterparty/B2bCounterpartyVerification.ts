/** 거래처 검증 정보 */
export type B2bCounterpartyVerification = {
	/** 외부 API 사용 ID */
	id: string
	/**
	 * 검증 시각
	 * (RFC 3339 date-time)
	 */
	checkedAt: string
}
