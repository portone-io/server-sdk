import type { PageInfo } from "./../../common/PageInfo"
import type { PlatformAccountTransfer } from "./../../platform/accountTransfer/PlatformAccountTransfer"
import type { PlatformAccountTransferStatusStats } from "./../../platform/PlatformAccountTransferStatusStats"
/** 이체내역 다건 조회 성공 응답 정보 */
export type GetPlatformAccountTransfersResponse = {
	/** 조회된 이체내역 리스트 */
	items: PlatformAccountTransfer[]
	/** 조회된 페이지 정보 */
	page: PageInfo
	/** 이체 내역 상태별 건 수 */
	counts: PlatformAccountTransferStatusStats
}
