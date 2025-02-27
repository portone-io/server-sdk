import type { DisputeStatus } from "./../payment/DisputeStatus"
/** 분쟁 내역 */
export type Dispute = {
	/** 분쟁 상태 */
	status: DisputeStatus
	/** PG사 분쟁 아이디 */
	pgDisputeId?: string
	/** 분쟁 사유 */
	reason: string
	/**
	 * 분쟁 발생 시각
	 * (RFC 3339 date-time)
	 */
	createdAt: string
	/**
	 * 분쟁 해소 시각
	 * (RFC 3339 date-time)
	 */
	resolvedAt?: string
}
