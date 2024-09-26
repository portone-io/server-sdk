/** 플랫폼 파트너 상태 */
export type PlatformPartnerStatus =
	/** 승인 대기 중 */
	| "PENDING"
	/** 승인 완료 */
	| "APPROVED"
	/** 승인 거절 */
	| "REJECTED"
