import type { FailedPaymentSchedule } from "#generated/payment/paymentSchedule/FailedPaymentSchedule"
import type { PendingPaymentSchedule } from "#generated/payment/paymentSchedule/PendingPaymentSchedule"
import type { RevokedPaymentSchedule } from "#generated/payment/paymentSchedule/RevokedPaymentSchedule"
import type { ScheduledPaymentSchedule } from "#generated/payment/paymentSchedule/ScheduledPaymentSchedule"
import type { StartedPaymentSchedule } from "#generated/payment/paymentSchedule/StartedPaymentSchedule"
import type { SucceededPaymentSchedule } from "#generated/payment/paymentSchedule/SucceededPaymentSchedule"

/** 결제 예약 건 */
export type PaymentSchedule =
	/** 결제 실패 */
	| FailedPaymentSchedule
	/** 결제 완료 대기 */
	| PendingPaymentSchedule
	/** 취소된 결제 예약 */
	| RevokedPaymentSchedule
	/** 결제 예약 완료 */
	| ScheduledPaymentSchedule
	/** 결제 시작 */
	| StartedPaymentSchedule
	/** 결제 성공 */
	| SucceededPaymentSchedule
