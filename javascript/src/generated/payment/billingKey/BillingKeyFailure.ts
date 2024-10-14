/** 발급 실패 상세 정보 */
export type BillingKeyFailure = {
	/** 실패 사유 */
	message?: string
	/** PG사 실패 코드 */
	pgCode?: string
	/** PG사 실패 사유 */
	pgMessage?: string
	/**
	 * 실패 시점
	 * (RFC 3339 date-time)
	 */
	failedAt: string
}
