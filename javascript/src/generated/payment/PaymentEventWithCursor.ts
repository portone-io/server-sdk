import type { PaymentEvent } from "./../payment/PaymentEvent"
/** 결제 이벤트 및 커서 정보 */
export type PaymentEventWithCursor = {
	/** 결제 이벤트 정보 */
	paymentEvent: PaymentEvent
	/** 해당 결제 이벤트의 커서 정보 */
	cursor: string
}
