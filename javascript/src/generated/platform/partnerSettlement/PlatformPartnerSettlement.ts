import type { PlatformPartnerManualSettlement } from "./../../platform/partnerSettlement/PlatformPartnerManualSettlement"
import type { PlatformPartnerOrderCancelSettlement } from "./../../platform/partnerSettlement/PlatformPartnerOrderCancelSettlement"
import type { PlatformPartnerOrderSettlement } from "./../../platform/partnerSettlement/PlatformPartnerOrderSettlement"

export type PlatformPartnerSettlement =
	| PlatformPartnerManualSettlement
	| PlatformPartnerOrderSettlement
	| PlatformPartnerOrderCancelSettlement
