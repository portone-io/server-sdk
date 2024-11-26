import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformAdditionalFeePolicy } from "./../../platform/PlatformAdditionalFeePolicy"
/** 추가 수수료 정책 다건 조회 성공 응답 정보 */
export type GetPlatformAdditionalFeePoliciesResponse = {
	/** 조회된 추가 수수료 정책 리스트 */
	items: PlatformAdditionalFeePolicy[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
