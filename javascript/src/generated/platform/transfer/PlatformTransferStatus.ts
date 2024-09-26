/** 정산 상태 */
export type PlatformTransferStatus =
	/** 정산 완료 */
	| "SETTLED"
	/** 정산 예약 */
	| "SCHEDULED"
	/** 지급 완료 */
	| "PAID_OUT"
	/** 정산 중 */
	| "IN_PROCESS"
	/** 지급 중 */
	| "IN_PAYOUT"
