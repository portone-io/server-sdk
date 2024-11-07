import type { Payment } from "./../payment/Payment"

/** 결제 건 및 커서 정보 */
export type PaymentWithCursor = {
	/** 결제 건 정보 */
	payment: Payment
	/** 해당 결제 건의 커서 정보 */
	cursor: string
}
