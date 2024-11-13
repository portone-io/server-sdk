/** 빌링키가 삭제되었을 때 이벤트의 실제 세부 내용입니다. */
export type WebhookBillingKeyDataDeleted = {
	/** 포트원에서 채번한 빌링키입니다. */
	billingKey: string
}
