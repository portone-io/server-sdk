import type { PageInput } from "./../../common/PageInput"
import type { PlatformPartnerFilterInput } from "./../../platform/PlatformPartnerFilterInput"
/** 파트너 다건 조회를 위한 입력 정보 */
export type GetPlatformPartnersBody = {
	/** 요청할 페이지 정보 */
	page?: PageInput
	/** 조회할 파트너 조건 필터 */
	filter?: PlatformPartnerFilterInput
}
