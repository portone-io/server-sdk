import type { PaymentCancellation } from "#generated/payment/PaymentCancellation"

/** 결제 취소 성공 응답 */
export type CancelPaymentResponse = {
	/** 결체 취소 내역 */
	cancellation: PaymentCancellation
}
