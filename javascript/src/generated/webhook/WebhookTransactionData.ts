import type { WebhookTransactionCancelledData } from "./WebhookTransactionCancelledData"
import type { WebhookTransactionDataConfirm } from "./WebhookTransactionDataConfirm"
import type { WebhookTransactionDataDisputeCreated } from "./WebhookTransactionDataDisputeCreated"
import type { WebhookTransactionDataDisputeResolved } from "./WebhookTransactionDataDisputeResolved"
import type { WebhookTransactionDataFailed } from "./WebhookTransactionDataFailed"
import type { WebhookTransactionDataPaid } from "./WebhookTransactionDataPaid"
import type { WebhookTransactionDataPayPending } from "./WebhookTransactionDataPayPending"
import type { WebhookTransactionDataReady } from "./WebhookTransactionDataReady"
import type { WebhookTransactionDataVirtualAccountIssued } from "./WebhookTransactionDataVirtualAccountIssued"
/** 결제 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다. */
export type WebhookTransactionData =
	| WebhookTransactionDataReady
	| WebhookTransactionDataPaid
	| WebhookTransactionDataVirtualAccountIssued
	| WebhookTransactionDataFailed
	| WebhookTransactionDataPayPending
	| WebhookTransactionDataConfirm
	| WebhookTransactionDataDisputeCreated
	| WebhookTransactionDataDisputeResolved
	| WebhookTransactionCancelledData
