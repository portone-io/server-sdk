import type { PlatformBulkPayoutStats } from "./../../platform/bulkPayout/PlatformBulkPayoutStats"
import type { PlatformBulkPayoutStatus } from "./../../platform/bulkPayout/PlatformBulkPayoutStatus"
import type { PlatformPayoutMethod } from "./../../platform/PlatformPayoutMethod"
export type PlatformBulkPayout = {
	/** 일괄 지급 고유 아이디 */
	id: string
	graphqlId: string
	/** 이름 */
	name: string
	/** 생성자 아이디 */
	creatorId: string
	/** 지급 유형 */
	method: PlatformPayoutMethod
	/**
	 * 총 지급 금액
	 * (int64)
	 */
	totalPayoutAmount: number
	/**
	 * 총 정산 금액
	 * (int64)
	 */
	totalSettlementAmount: number
	/** 상태 */
	status: PlatformBulkPayoutStatus
	/** 지급 통계 */
	payoutStats: PlatformBulkPayoutStats
	/**
	 * 상태 업데이트 일시
	 * (RFC 3339 date-time)
	 */
	statusUpdatedAt: string
	/**
	 * 생성 일시
	 * (RFC 3339 date-time)
	 */
	createdAt: string
	/**
	 * 업데이트 일시
	 * (RFC 3339 date-time)
	 */
	updatedAt: string
}
