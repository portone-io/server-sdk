import type { PlatformPartner } from "./../../platform/PlatformPartner"
/** 파트너 다건 생성 성공 응답 */
export type CreatePlatformPartnersResponse = {
	/** 생성된 파트너 리스트 */
	partners: PlatformPartner[]
}
