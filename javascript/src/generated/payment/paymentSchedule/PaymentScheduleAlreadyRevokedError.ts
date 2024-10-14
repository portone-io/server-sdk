/** 결제 예약건이 이미 취소된 경우 */
export type PaymentScheduleAlreadyRevokedError = {
	type: "PAYMENT_SCHEDULE_ALREADY_REVOKED"
	message?: string
}
