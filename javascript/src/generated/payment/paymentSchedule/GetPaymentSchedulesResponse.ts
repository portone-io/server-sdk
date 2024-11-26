import type { PageInfo } from "./../../common/PageInfo"
import type { PaymentSchedule } from "./../../payment/paymentSchedule/PaymentSchedule"
/** 결제 예약 다건 조회 성공 응답 정보 */
export type GetPaymentSchedulesResponse = {
	/** 조회된 결제 예약 건 리스트 */
	items: PaymentSchedule[]
	/** 조회된 페이지 정보 */
	page: PageInfo
}
