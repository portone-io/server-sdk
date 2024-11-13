import type { WebhookTransactionDataPaid } from "./WebhookTransactionDataPaid"

/** 결제(예약 결제 포함)가 승인되었을 때 (모든 결제 수단) */
export type WebhookTransactionPaid = {
	/** 웹훅을 트리거한 이벤트의 타입입니다. */
	type: "Transaction.Paid"
	/**
	 * 해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다.
	 * (RFC 3339 date-time)
	 */
	timestamp: string
	/** 결제(예약 결제 포함)가 승인되었을 때 이벤트의 실제 세부 내용입니다. (모든 결제 수단) */
	data: WebhookTransactionDataPaid
}
