/** 빌링키 발급이 실패했을 때 이벤트의 실제 세부 내용입니다. */
export type WebhookBillingKeyDataFailed = {
	/** 포트원에서 채번한 빌링키입니다. */
	billingKey: string
	/** 웹훅을 트리거한 상점의 아이디입니다. */
	storeId: string
}
