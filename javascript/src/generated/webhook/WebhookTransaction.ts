import type { WebhookTransactionCancelled } from "./WebhookTransactionCancelled"
import type { WebhookTransactionConfirm } from "./WebhookTransactionConfirm"
import type { WebhookTransactionDisputeCreated } from "./WebhookTransactionDisputeCreated"
import type { WebhookTransactionDisputeResolved } from "./WebhookTransactionDisputeResolved"
import type { WebhookTransactionFailed } from "./WebhookTransactionFailed"
import type { WebhookTransactionPaid } from "./WebhookTransactionPaid"
import type { WebhookTransactionPayPending } from "./WebhookTransactionPayPending"
import type { WebhookTransactionReady } from "./WebhookTransactionReady"
import type { WebhookTransactionVirtualAccountIssued } from "./WebhookTransactionVirtualAccountIssued"
/** 결제 관련 */
export type WebhookTransaction =
	| WebhookTransactionReady
	| WebhookTransactionPaid
	| WebhookTransactionVirtualAccountIssued
	| WebhookTransactionFailed
	| WebhookTransactionPayPending
	| WebhookTransactionConfirm
	| WebhookTransactionDisputeCreated
	| WebhookTransactionDisputeResolved
	| WebhookTransactionCancelled
