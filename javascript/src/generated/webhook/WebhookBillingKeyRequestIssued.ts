import type { WebhookBillingKeyRequestIssuedData } from "./../webhook/WebhookBillingKeyRequestIssuedData"

/** 빌링키가 발급되었을 때 */
export type WebhookBillingKeyRequestIssued = {
	/** 웹훅을 트리거한 이벤트의 타입입니다. */
	type: "BillingKey.Issued"
	/**
	 * 해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/** 웹훅을 트리거한 이벤트의 실제 세부 내용입니다. */
	data: WebhookBillingKeyRequestIssuedData
}
