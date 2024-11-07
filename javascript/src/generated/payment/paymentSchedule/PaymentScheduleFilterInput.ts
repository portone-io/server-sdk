import type { PaymentScheduleStatus } from "./../../payment/paymentSchedule/PaymentScheduleStatus"

/** 결제 예약 건 다건 조회를 위한 입력 정보 */
export type PaymentScheduleFilterInput = {
	/**
	 * 상점 아이디
	 *
	 * 접근 권한이 있는 상점 아이디만 입력 가능하며, 미입력시 토큰에 담긴 상점 아이디를 사용합니다.
	 */
	storeId?: string
	/** 빌링키 */
	billingKey?: string
	/**
	 * 결제 예정 시점 조건 범위의 시작
	 *
	 * 값을 입력하지 않으면 파라미터 end의 90일 전으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	from?: string
	/**
	 * 결제 예정 시점 조건 범위의 끝
	 *
	 * 값을 입력하지 않으면 현재 시점으로 설정됩니다.
	 * (RFC 3339 date-time)
	 */
	until?: string
	/**
	 * 결제 예약 건 상태 리스트
	 *
	 * 값을 입력하지 않으면 상태 필터링이 적용되지 않습니다.
	 */
	status?: PaymentScheduleStatus[]
}
