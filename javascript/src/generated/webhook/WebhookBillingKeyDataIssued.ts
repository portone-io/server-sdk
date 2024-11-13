/** 빌링키가 발급되었을 때 이벤트의 실제 세부 내용입니다. */
export type WebhookBillingKeyDataIssued = {
	/** 포트원에서 채번한 빌링키입니다. */
	billingKey: string
}
