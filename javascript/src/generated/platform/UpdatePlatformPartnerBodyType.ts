import type { UpdatePlatformPartnerBodyTypeBusiness } from "#generated/platform/UpdatePlatformPartnerBodyTypeBusiness"
import type { UpdatePlatformPartnerBodyTypeNonWhtPayer } from "#generated/platform/UpdatePlatformPartnerBodyTypeNonWhtPayer"
import type { UpdatePlatformPartnerBodyTypeWhtPayer } from "#generated/platform/UpdatePlatformPartnerBodyTypeWhtPayer"

/**
 * 파트너 업데이트를 위한 유형별 추가 정보
 *
 * 파트너 유형별 추가 정보를 수정합니다.
 * 기존과 다른 파트너 유형 정보가 입력된 경우, 파트너의 유형 자체가 변경됩니다.
 */
export type UpdatePlatformPartnerBodyType = {
	/** 사업자 추가 정보 */
	business?: UpdatePlatformPartnerBodyTypeBusiness
	/** 원천징수 대상자 추가 정보 */
	whtPayer?: UpdatePlatformPartnerBodyTypeWhtPayer
	/** 원천징수 비대상자 추가 정보 */
	nonWhtPayer?: UpdatePlatformPartnerBodyTypeNonWhtPayer
}
