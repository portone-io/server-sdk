import type { PlatformPartnerSettlement } from "#generated/platform/partnerSettlement/PlatformPartnerSettlement"

export type PlatformBulkPayoutPartnerSettlement = {
	bulkPayoutId: string
	partnerSettlement: PlatformPartnerSettlement
	isSelected: boolean
}
