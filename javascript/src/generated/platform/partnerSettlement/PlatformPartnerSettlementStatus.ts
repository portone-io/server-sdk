/** 정산 상태 */
export type PlatformPartnerSettlementStatus =
	/** 지급 예약 */
	| "PAYOUT_SCHEDULED"
	/** 지급 예정 */
	| "PAYOUT_PREPARED"
	/** 지급 보류 */
	| "PAYOUT_WITHHELD"
	/** 지급 실패 */
	| "PAYOUT_FAILED"
	/** 지급 중 */
	| "IN_PAYOUT"
	/** 지급 완료 */
	| "PAID_OUT"
