import type { CreatePlatformPartnerBodyTypeBusiness } from "./../../platform/partner/CreatePlatformPartnerBodyTypeBusiness"
import type { CreatePlatformPartnerBodyTypeNonWhtPayer } from "./../../platform/partner/CreatePlatformPartnerBodyTypeNonWhtPayer"
import type { CreatePlatformPartnerBodyTypeWhtPayer } from "./../../platform/partner/CreatePlatformPartnerBodyTypeWhtPayer"

/** 파트너 생성을 위한 유형별 추가 정보 */
export type CreatePlatformPartnerBodyType = {
	/** 사업자 추가 정보 */
	business?: CreatePlatformPartnerBodyTypeBusiness
	/** 원천징수 대상자 추가 정보 */
	whtPayer?: CreatePlatformPartnerBodyTypeWhtPayer
	/** 원천징수 비대상자 추가 정보 */
	nonWhtPayer?: CreatePlatformPartnerBodyTypeNonWhtPayer
}
