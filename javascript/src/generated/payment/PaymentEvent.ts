import type { Unrecognized } from "./../../utils/unrecognized"
import type { CancelledPaymentEvent } from "./../payment/CancelledPaymentEvent"
import type { PaidPaymentEvent } from "./../payment/PaidPaymentEvent"
import type { PartialCancelledPaymentEvent } from "./../payment/PartialCancelledPaymentEvent"
/** 결제 이벤트 */
export type PaymentEvent =
	/** 결제 취소 이벤트 */
	| CancelledPaymentEvent
	/** 결제 완료 이벤트 */
	| PaidPaymentEvent
	/** 결제 부분 취소 이벤트 */
	| PartialCancelledPaymentEvent
	| { readonly type: Unrecognized }

export function isUnrecognizedPaymentEvent(entity: PaymentEvent): entity is { readonly type: Unrecognized } {
	return entity.type !== "CANCELLED"
		&& entity.type !== "PAID"
		&& entity.type !== "PARTIAL_CANCELLED"
}
