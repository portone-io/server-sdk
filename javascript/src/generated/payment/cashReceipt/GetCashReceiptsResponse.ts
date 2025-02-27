import type { CashReceipt } from "./../../payment/cashReceipt/CashReceipt"
import type { PageInfo } from "./../../common/PageInfo"
/** 현금영수증 다건 조회 성공 응답 정보 */
export type GetCashReceiptsResponse = {
	/** 조회된 현금영수증 리스트 */
	items: CashReceipt[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
