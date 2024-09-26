import type { PlatformPartner } from "#generated/platform/PlatformPartner"

/** 파트너 승인 성공 응답 */
export type ApprovePlatformPartnerResponse = {
	/** 승인된 파트너 */
	partner: PlatformPartner
}
