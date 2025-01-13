import type { Unrecognized } from "./../../utils/unrecognized"
import type { CancelledPaymentTransaction } from "./../payment/CancelledPaymentTransaction"
import type { FailedPaymentTransaction } from "./../payment/FailedPaymentTransaction"
import type { PaidPaymentTransaction } from "./../payment/PaidPaymentTransaction"
import type { PartialCancelledPaymentTransaction } from "./../payment/PartialCancelledPaymentTransaction"
import type { PayPendingPaymentTransaction } from "./../payment/PayPendingPaymentTransaction"
import type { ReadyPaymentTransaction } from "./../payment/ReadyPaymentTransaction"
import type { VirtualAccountIssuedPaymentTransaction } from "./../payment/VirtualAccountIssuedPaymentTransaction"
/** 결제 시도 */
export type PaymentTransaction =
	/** 결제 취소 */
	| CancelledPaymentTransaction
	/** 결제 실패 */
	| FailedPaymentTransaction
	/** 결제 완료 */
	| PaidPaymentTransaction
	/** 결제 부분 취소 */
	| PartialCancelledPaymentTransaction
	/** 결제 완료 대기 */
	| PayPendingPaymentTransaction
	/** 결제 준비 */
	| ReadyPaymentTransaction
	/** 가상계좌 발급 완료 */
	| VirtualAccountIssuedPaymentTransaction
	| { readonly status: Unrecognized }

export function isUnrecognizedPaymentTransaction(entity: PaymentTransaction): entity is { readonly status: Unrecognized } {
	return entity.status !== "CANCELLED"
		&& entity.status !== "FAILED"
		&& entity.status !== "PAID"
		&& entity.status !== "PARTIAL_CANCELLED"
		&& entity.status !== "PAY_PENDING"
		&& entity.status !== "READY"
		&& entity.status !== "VIRTUAL_ACCOUNT_ISSUED"
}
