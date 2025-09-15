import type { PlatformPayoutSettlementStatementStatus } from "./../../platform/payout/PlatformPayoutSettlementStatementStatus"
/** 정산 내역서 요약 정보 */
export type PlatformPayoutSettlementStatementSummary = {
	/** 상태 */
	status: PlatformPayoutSettlementStatementStatus
	/** 아이디 */
	id?: string
	/**
	 * 발송 일시
	 * (RFC 3339 date-time)
	 */
	issuedAt?: string
}
