import {
  webhookBillingKey,
  webhookBillingKeyData,
  webhookBillingKeyDataVariants,
  webhookBillingKeyVariants,
} from "./billingKey.ts"
import { webhook } from "./common.ts"
import { extractDiscriminant } from "./definition.ts"
import {
  webhookTransaction,
  webhookTransactionCancelled,
  webhookTransactionCancelledData,
  webhookTransactionData,
  webhookTransactionDataVariants,
  webhookTransactionVariants,
} from "./transaction.ts"

export const entities = [
  webhook,
  webhookTransaction,
  webhookTransactionCancelled,
  ...webhookTransactionVariants,
  webhookTransactionData,
  webhookTransactionCancelledData,
  ...webhookTransactionDataVariants,
  webhookBillingKey,
  ...webhookBillingKeyVariants,
  webhookBillingKeyData,
  ...webhookBillingKeyDataVariants,
]

export const types = [
  ...webhookTransactionVariants.flatMap(extractDiscriminant),
  ...webhookBillingKeyVariants.flatMap(extractDiscriminant),
]

export const prefixes = [
  "Transaction",
  "BillingKey",
]
