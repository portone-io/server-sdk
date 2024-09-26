import type { PaymentScheduleSummary } from "#generated/paymentSchedule/PaymentScheduleSummary"

/** 결제 예약 성공 응답 */
export type CreatePaymentScheduleResponse = {
	/** 결제 예약 건 */
	schedule: PaymentScheduleSummary
}
