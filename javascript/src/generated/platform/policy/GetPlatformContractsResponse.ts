import type { PageInfo } from "#generated/common/PageInfo"
import type { PlatformContract } from "#generated/platform/PlatformContract"

/** 계약 다건 조회 성공 응답 */
export type GetPlatformContractsResponse = {
	/** 조회된 계약 리스트 */
	items: PlatformContract[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
