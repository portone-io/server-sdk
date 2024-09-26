import type { PlatformPartnerSettlementStatus } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementStatus"

export type PlatformBulkPayoutPartnerSettlementsFilterInput = {
	partnerIds: string[]
	/** 정산 상태 */
	statuses: PlatformPartnerSettlementStatus[]
}
