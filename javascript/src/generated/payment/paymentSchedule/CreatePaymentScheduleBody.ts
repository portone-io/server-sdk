import type { BillingKeyPaymentInput } from "#generated/common/BillingKeyPaymentInput"

/** 결제 예약 요청 입력 정보 */
export type CreatePaymentScheduleBody = {
	/** 빌링키 결제 입력 정보 */
	payment: BillingKeyPaymentInput
	/**
	 * 결제 예정 시점
	 * (RFC 3339 date-time)
	 */
	timeToPay: string
}
