export type { Webhook } from "./Webhook"
export type { WebhookBillingKey } from "./WebhookBillingKey"
export type { WebhookBillingKeyData } from "./WebhookBillingKeyData"
export type { WebhookBillingKeyDataDeleted } from "./WebhookBillingKeyDataDeleted"
export type { WebhookBillingKeyDataFailed } from "./WebhookBillingKeyDataFailed"
export type { WebhookBillingKeyDataIssued } from "./WebhookBillingKeyDataIssued"
export type { WebhookBillingKeyDataReady } from "./WebhookBillingKeyDataReady"
export type { WebhookBillingKeyDataUpdated } from "./WebhookBillingKeyDataUpdated"
export type { WebhookBillingKeyDeleted } from "./WebhookBillingKeyDeleted"
export type { WebhookBillingKeyFailed } from "./WebhookBillingKeyFailed"
export type { WebhookBillingKeyIssued } from "./WebhookBillingKeyIssued"
export type { WebhookBillingKeyReady } from "./WebhookBillingKeyReady"
export type { WebhookBillingKeyUpdated } from "./WebhookBillingKeyUpdated"
export type { WebhookTransaction } from "./WebhookTransaction"
export type { WebhookTransactionCancelled } from "./WebhookTransactionCancelled"
export type { WebhookTransactionCancelledCancelled } from "./WebhookTransactionCancelledCancelled"
export type { WebhookTransactionCancelledData } from "./WebhookTransactionCancelledData"
export type { WebhookTransactionCancelledDataCancelled } from "./WebhookTransactionCancelledDataCancelled"
export type { WebhookTransactionCancelledDataPartialCancelled } from "./WebhookTransactionCancelledDataPartialCancelled"
export type { WebhookTransactionCancelledPartialCancelled } from "./WebhookTransactionCancelledPartialCancelled"
export type { WebhookTransactionCancelPending } from "./WebhookTransactionCancelPending"
export type { WebhookTransactionData } from "./WebhookTransactionData"
export type { WebhookTransactionDataCancelPending } from "./WebhookTransactionDataCancelPending"
export type { WebhookTransactionDataFailed } from "./WebhookTransactionDataFailed"
export type { WebhookTransactionDataPaid } from "./WebhookTransactionDataPaid"
export type { WebhookTransactionDataPayPending } from "./WebhookTransactionDataPayPending"
export type { WebhookTransactionDataReady } from "./WebhookTransactionDataReady"
export type { WebhookTransactionDataVirtualAccountIssued } from "./WebhookTransactionDataVirtualAccountIssued"
export type { WebhookTransactionFailed } from "./WebhookTransactionFailed"
export type { WebhookTransactionPaid } from "./WebhookTransactionPaid"
export type { WebhookTransactionPayPending } from "./WebhookTransactionPayPending"
export type { WebhookTransactionReady } from "./WebhookTransactionReady"
export type { WebhookTransactionVirtualAccountIssued } from "./WebhookTransactionVirtualAccountIssued"
import type { Webhook } from "./Webhook"
import type { Unrecognized } from "../../utils/unrecognized"

export function isUnrecognizedWebhook(entity: Webhook): entity is { readonly type: Unrecognized } {
	return entity.type !== "Transaction.Ready"
		&& entity.type !== "Transaction.Paid"
		&& entity.type !== "Transaction.VirtualAccountIssued"
		&& entity.type !== "Transaction.PartialCancelled"
		&& entity.type !== "Transaction.Cancelled"
		&& entity.type !== "Transaction.Failed"
		&& entity.type !== "Transaction.PayPending"
		&& entity.type !== "Transaction.CancelPending"
		&& entity.type !== "BillingKey.Ready"
		&& entity.type !== "BillingKey.Issued"
		&& entity.type !== "BillingKey.Failed"
		&& entity.type !== "BillingKey.Deleted"
		&& entity.type !== "BillingKey.Updated"
}
