import type { CancelledPayment } from "#generated/payment/CancelledPayment"
import type { FailedPayment } from "#generated/payment/FailedPayment"
import type { PaidPayment } from "#generated/payment/PaidPayment"
import type { PartialCancelledPayment } from "#generated/payment/PartialCancelledPayment"
import type { PayPendingPayment } from "#generated/payment/PayPendingPayment"
import type { ReadyPayment } from "#generated/payment/ReadyPayment"
import type { VirtualAccountIssuedPayment } from "#generated/payment/VirtualAccountIssuedPayment"

/** 결제 건 */
export type Payment =
	/** 결제 취소 */
	| CancelledPayment
	/** 결제 실패 */
	| FailedPayment
	/** 결제 완료 */
	| PaidPayment
	/** 결제 부분 취소 */
	| PartialCancelledPayment
	/** 결제 완료 대기 */
	| PayPendingPayment
	/** 결제 준비 */
	| ReadyPayment
	/** 가상계좌 발급 완료 */
	| VirtualAccountIssuedPayment
