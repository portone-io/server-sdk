import type { Unrecognized } from "./../../utils/unrecognized"
import type { PlatformPartnerTypeBusiness } from "./../platform/PlatformPartnerTypeBusiness"
import type { PlatformPartnerTypeNonWhtPayer } from "./../platform/PlatformPartnerTypeNonWhtPayer"
import type { PlatformPartnerTypeWhtPayer } from "./../platform/PlatformPartnerTypeWhtPayer"
/** 파트너 유형별 추가 정보 */
export type PlatformPartnerType =
	/** 사업자 파트너 정보 */
	| PlatformPartnerTypeBusiness
	/** 원천징수 비대상자 파트너 정보 */
	| PlatformPartnerTypeNonWhtPayer
	/** 원천징수 대상자 파트너 정보 */
	| PlatformPartnerTypeWhtPayer
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformPartnerType(entity: PlatformPartnerType): entity is { readonly type: Unrecognized } {
	return entity.type !== "BUSINESS"
		&& entity.type !== "NON_WHT_PAYER"
		&& entity.type !== "WHT_PAYER"
}
