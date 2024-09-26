import type { FailedPaymentCancellation } from "#generated/payment/FailedPaymentCancellation"
import type { RequestedPaymentCancellation } from "#generated/payment/RequestedPaymentCancellation"
import type { SucceededPaymentCancellation } from "#generated/payment/SucceededPaymentCancellation"

/** 결제 취소 내역 */
export type PaymentCancellation =
	/** 취소 실패 */
	| FailedPaymentCancellation
	/** 취소 요청 */
	| RequestedPaymentCancellation
	/** 취소 완료 */
	| SucceededPaymentCancellation
