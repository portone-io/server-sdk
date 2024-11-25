import type { Unrecognized } from "../../utils/unrecognized"
import type { WebhookBillingKey } from "./WebhookBillingKey"
import type { WebhookTransaction } from "./WebhookTransaction"
/** 2024-04-25 버전의 웹훅 형식 */
export type Webhook =
	| WebhookTransaction
	| WebhookBillingKey
	| { readonly type: Unrecognized }
