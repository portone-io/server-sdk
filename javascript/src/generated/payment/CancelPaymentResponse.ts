import type { PaymentCancellation } from "./../payment/PaymentCancellation"
/** 결제 취소 성공 응답 */
export type CancelPaymentResponse = {
	/** 결제 취소 내역 */
	cancellation: PaymentCancellation
}
