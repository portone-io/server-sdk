import type { WebhookBillingKeyDataDeleted } from "./WebhookBillingKeyDataDeleted"
import type { WebhookBillingKeyDataFailed } from "./WebhookBillingKeyDataFailed"
import type { WebhookBillingKeyDataIssued } from "./WebhookBillingKeyDataIssued"
import type { WebhookBillingKeyDataReady } from "./WebhookBillingKeyDataReady"
import type { WebhookBillingKeyDataUpdated } from "./WebhookBillingKeyDataUpdated"

/** 빌링키 발급 관련 웹훅을 트리거한 이벤트의 실제 세부 내용입니다. */
export type WebhookBillingKeyData =
	| WebhookBillingKeyDataReady
	| WebhookBillingKeyDataIssued
	| WebhookBillingKeyDataFailed
	| WebhookBillingKeyDataDeleted
	| WebhookBillingKeyDataUpdated
