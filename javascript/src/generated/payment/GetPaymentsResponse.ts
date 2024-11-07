import type { PageInfo } from "./../common/PageInfo"
import type { Payment } from "./../payment/Payment"

/** 결제 건 다건 조회 성공 응답 정보 */
export type GetPaymentsResponse = {
	/** 조회된 결제 건 리스트 */
	items: Payment[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
