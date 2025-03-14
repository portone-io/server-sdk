import type { Unrecognized } from "./../../utils/unrecognized"
import type { CancelledPayment } from "./../payment/CancelledPayment"
import type { FailedPayment } from "./../payment/FailedPayment"
import type { PaidPayment } from "./../payment/PaidPayment"
import type { PartialCancelledPayment } from "./../payment/PartialCancelledPayment"
import type { PayPendingPayment } from "./../payment/PayPendingPayment"
import type { ReadyPayment } from "./../payment/ReadyPayment"
import type { VirtualAccountIssuedPayment } from "./../payment/VirtualAccountIssuedPayment"
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
	| { readonly status: Unrecognized }

export function isUnrecognizedPayment(entity: Payment): entity is { readonly status: Unrecognized } {
	return entity.status !== "CANCELLED"
		&& entity.status !== "FAILED"
		&& entity.status !== "PAID"
		&& entity.status !== "PARTIAL_CANCELLED"
		&& entity.status !== "PAY_PENDING"
		&& entity.status !== "READY"
		&& entity.status !== "VIRTUAL_ACCOUNT_ISSUED"
}
