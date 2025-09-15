/** 빌링키 발급 및 초회 결제 수동 승인 완료 응답 */
export type ConfirmedBillingKeyIssueAndPaySummary = {
	/** 빌링키 */
	billingKey: string
	/** 결제 건 아이디 */
	paymentId: string
}
