import type { WebhookTransactionCancelledData } from "./WebhookTransactionCancelledData"
import type { WebhookTransactionDataCancelPending } from "./WebhookTransactionDataCancelPending"
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
	| WebhookTransactionDataCancelPending
	| WebhookTransactionCancelledData