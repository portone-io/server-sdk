import type { PlatformPartner } from "#generated/platform/PlatformPartner"

/** 파트너 거절 성공 응답 */
export type RejectPlatformPartnerResponse = {
	/** 거절된 파트너 */
	partner: PlatformPartner
}
