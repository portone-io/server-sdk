/** 결제 예약건이 이미 존재하는 경우 */
export type PaymentScheduleAlreadyExistsError = {
	type: "PAYMENT_SCHEDULE_ALREADY_EXISTS"
	message?: string
}
