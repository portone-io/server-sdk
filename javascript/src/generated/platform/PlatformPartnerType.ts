import type { PlatformPartnerTypeBusiness } from "#generated/platform/PlatformPartnerTypeBusiness"
import type { PlatformPartnerTypeNonWhtPayer } from "#generated/platform/PlatformPartnerTypeNonWhtPayer"
import type { PlatformPartnerTypeWhtPayer } from "#generated/platform/PlatformPartnerTypeWhtPayer"

/** 파트너 유형별 추가 정보 */
export type PlatformPartnerType =
	/** 사업자 파트너 정보 */
	| PlatformPartnerTypeBusiness
	/** 원천징수 비대상자 파트너 정보 */
	| PlatformPartnerTypeNonWhtPayer
	/** 원천징수 대상자 파트너 정보 */
	| PlatformPartnerTypeWhtPayer
