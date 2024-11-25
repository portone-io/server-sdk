import type { WebhookBillingKeyDeleted } from "./WebhookBillingKeyDeleted"
import type { WebhookBillingKeyFailed } from "./WebhookBillingKeyFailed"
import type { WebhookBillingKeyIssued } from "./WebhookBillingKeyIssued"
import type { WebhookBillingKeyReady } from "./WebhookBillingKeyReady"
import type { WebhookBillingKeyUpdated } from "./WebhookBillingKeyUpdated"
/** 빌링키 발급 관련 */
export type WebhookBillingKey =
	| WebhookBillingKeyReady
	| WebhookBillingKeyIssued
	| WebhookBillingKeyFailed
	| WebhookBillingKeyDeleted
	| WebhookBillingKeyUpdated
