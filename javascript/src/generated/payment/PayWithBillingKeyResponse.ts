import type { BillingKeyPaymentSummary } from "#generated/payment/BillingKeyPaymentSummary"

/** 빌링키 결제 성공 응답 */
export type PayWithBillingKeyResponse = {
	/** 결제 건 요약 정보 */
	payment: BillingKeyPaymentSummary
}
