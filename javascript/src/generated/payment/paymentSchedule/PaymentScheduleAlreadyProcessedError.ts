/** 결제 예약건이 이미 처리된 경우 */
export type PaymentScheduleAlreadyProcessedError = {
	type: "PAYMENT_SCHEDULE_ALREADY_PROCESSED"
	message?: string
}
