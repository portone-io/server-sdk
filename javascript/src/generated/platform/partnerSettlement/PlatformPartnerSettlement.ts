import type { PlatformPartnerManualSettlement } from "#generated/platform/partnerSettlement/PlatformPartnerManualSettlement"
import type { PlatformPartnerOrderCancelSettlement } from "#generated/platform/partnerSettlement/PlatformPartnerOrderCancelSettlement"
import type { PlatformPartnerOrderSettlement } from "#generated/platform/partnerSettlement/PlatformPartnerOrderSettlement"

export type PlatformPartnerSettlement =
	| PlatformPartnerManualSettlement
	| PlatformPartnerOrderSettlement
	| PlatformPartnerOrderCancelSettlement
