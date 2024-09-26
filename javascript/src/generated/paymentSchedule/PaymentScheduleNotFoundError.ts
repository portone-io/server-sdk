/** 결제 예약건이 존재하지 않는 경우 */
export type PaymentScheduleNotFoundError = {
	type: "PAYMENT_SCHEDULE_NOT_FOUND"
	message?: string
}
