import type { InstantPaymentSummary } from "#generated/payment/InstantPaymentSummary"

/** 수기 결제 성공 응답 */
export type PayInstantlyResponse = {
	/** 결제 건 요약 정보 */
	payment: InstantPaymentSummary
}
