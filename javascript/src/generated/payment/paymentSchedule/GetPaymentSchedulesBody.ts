import type { PageInput } from "./../../common/PageInput"
import type { PaymentScheduleFilterInput } from "./../../payment/paymentSchedule/PaymentScheduleFilterInput"
import type { PaymentScheduleSortInput } from "./../../payment/paymentSchedule/PaymentScheduleSortInput"

/**
 * 결제 예약 다건 조회를 위한 입력 정보
 *
 * 조회 결과는 결제 예정 시점(timeToPay) 기준 최신 순으로 정렬됩니다.
 */
export type GetPaymentSchedulesBody = {
	/**
	 * 요청할 페이지 정보
	 *
	 * 미 입력 시 number: 0, size: 10 으로 기본값이 적용됩니다.
	 */
	page?: PageInput
	/**
	 * 정렬 조건
	 *
	 * 미 입력 시 sortBy: TIME_TO_PAY, sortOrder: DESC 으로 기본값이 적용됩니다.
	 */
	sort?: PaymentScheduleSortInput
	/** 조회할 결제 예약 건의 조건 필터 */
	filter?: PaymentScheduleFilterInput
}
