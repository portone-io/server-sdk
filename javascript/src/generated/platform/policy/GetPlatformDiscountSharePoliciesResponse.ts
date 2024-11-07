import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformDiscountSharePolicy } from "./../../platform/PlatformDiscountSharePolicy"

/** 할인 분담 정책 다건 조회 성공 응답 정보 */
export type GetPlatformDiscountSharePoliciesResponse = {
	/** 조회된 할인 분담 정책 리스트 */
	items: PlatformDiscountSharePolicy[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
