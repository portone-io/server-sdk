import type { PlatformPartnerSettlementStatus } from "#generated/platform/partnerSettlement/PlatformPartnerSettlementStatus"

export type UpdatePlatformPartnerSettlementStatusBody = {
	partnerSettlementId: string
	status: PlatformPartnerSettlementStatus
	memo?: string
}
