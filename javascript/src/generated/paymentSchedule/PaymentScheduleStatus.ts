/** 결제 예약 건 상태 */
export type PaymentScheduleStatus =
	/** 예약 완료 */
	| "SCHEDULED"
	/** 결제 시작 */
	| "STARTED"
	/** 결제 성공 */
	| "SUCCEEDED"
	/** 결제 실패 */
	| "FAILED"
	/** 취소된 결제 예약 */
	| "REVOKED"
	/** 결제 승인 대기 */
	| "PENDING"
