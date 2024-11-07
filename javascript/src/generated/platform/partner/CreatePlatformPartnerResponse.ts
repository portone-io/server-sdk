import type { PlatformPartner } from "./../../platform/PlatformPartner"

/** 파트너 생성 성공 응답 */
export type CreatePlatformPartnerResponse = {
	/** 생성된 파트너 */
	partner: PlatformPartner
}
