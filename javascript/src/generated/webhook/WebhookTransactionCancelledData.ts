import type { WebhookTransactionCancelledDataCancelled } from "./WebhookTransactionCancelledDataCancelled"
import type { WebhookTransactionCancelledDataPartialCancelled } from "./WebhookTransactionCancelledDataPartialCancelled"
/** 결제 취소 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다. */
export type WebhookTransactionCancelledData =
	| WebhookTransactionCancelledDataPartialCancelled
	| WebhookTransactionCancelledDataCancelled
