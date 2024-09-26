import type { FailedPaymentSchedule } from "#generated/paymentSchedule/FailedPaymentSchedule"
import type { PendingPaymentSchedule } from "#generated/paymentSchedule/PendingPaymentSchedule"
import type { RevokedPaymentSchedule } from "#generated/paymentSchedule/RevokedPaymentSchedule"
import type { ScheduledPaymentSchedule } from "#generated/paymentSchedule/ScheduledPaymentSchedule"
import type { StartedPaymentSchedule } from "#generated/paymentSchedule/StartedPaymentSchedule"
import type { SucceededPaymentSchedule } from "#generated/paymentSchedule/SucceededPaymentSchedule"

/** 결제 예약 건 */
export type PaymentSchedule =
	/** 결제 실패 */
	| FailedPaymentSchedule
	/** 결제 대기 */
	| PendingPaymentSchedule
	/** 취소된 결제 예약 */
	| RevokedPaymentSchedule
	/** 결제 예약 완료 */
	| ScheduledPaymentSchedule
	/** 결제 시작 */
	| StartedPaymentSchedule
	/** 결제 성공 */
	| SucceededPaymentSchedule
