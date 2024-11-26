import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PlatformPartnerManualSettlement } from "./../../platform/partnerSettlement/PlatformPartnerManualSettlement"
import type { PlatformPartnerOrderCancelSettlement } from "./../../platform/partnerSettlement/PlatformPartnerOrderCancelSettlement"
import type { PlatformPartnerOrderSettlement } from "./../../platform/partnerSettlement/PlatformPartnerOrderSettlement"
export type PlatformPartnerSettlement =
	| PlatformPartnerManualSettlement
	| PlatformPartnerOrderSettlement
	| PlatformPartnerOrderCancelSettlement
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformPartnerSettlement(entity: PlatformPartnerSettlement): entity is { readonly type: Unrecognized } {
	return entity.type !== "MANUAL"
		&& entity.type !== "ORDER"
		&& entity.type !== "ORDER_CANCEL"
}
