import type { WebhookTransactionCancelledCancelled } from "./WebhookTransactionCancelledCancelled"
import type { WebhookTransactionCancelledPartialCancelled } from "./WebhookTransactionCancelledPartialCancelled"

/** 결제 취소 관련 */
export type WebhookTransactionCancelled =
	| WebhookTransactionCancelledPartialCancelled
	| WebhookTransactionCancelledCancelled
