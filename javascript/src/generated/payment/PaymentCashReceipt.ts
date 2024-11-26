import type { Unrecognized } from "./../../utils/unrecognized"
import type { CancelledPaymentCashReceipt } from "./../payment/CancelledPaymentCashReceipt"
import type { IssuedPaymentCashReceipt } from "./../payment/IssuedPaymentCashReceipt"
/** 결제 건 내 현금영수증 정보 */
export type PaymentCashReceipt =
	/** 발급 취소 */
	| CancelledPaymentCashReceipt
	/** 발급 완료 */
	| IssuedPaymentCashReceipt
	| { readonly status: Unrecognized }

export function isUnrecognizedPaymentCashReceipt(entity: PaymentCashReceipt): entity is { readonly status: Unrecognized } {
	return entity.status !== "CANCELLED"
		&& entity.status !== "ISSUED"
}
