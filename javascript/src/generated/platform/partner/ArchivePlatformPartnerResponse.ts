import type { PlatformPartner } from "./../../platform/PlatformPartner"

/** 파트너 보관 성공 응답 */
export type ArchivePlatformPartnerResponse = {
	/** 보관된 파트너 */
	partner: PlatformPartner
}
