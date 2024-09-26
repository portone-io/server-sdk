import type { PageInfo } from "#generated/common/PageInfo"
import type { PlatformPartner } from "#generated/platform/PlatformPartner"

/** 파트너 다건 조회 성공 응답 정보 */
export type GetPlatformPartnersResponse = {
	/** 조회된 파트너 리스트 */
	items: PlatformPartner[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
