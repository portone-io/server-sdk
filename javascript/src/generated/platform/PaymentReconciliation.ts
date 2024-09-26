import type { PaymentReconciliationIncomparable } from "#generated/platform/PaymentReconciliationIncomparable"
import type { PaymentReconciliationMatched } from "#generated/platform/PaymentReconciliationMatched"
import type { PaymentReconciliationNotCollected } from "#generated/platform/PaymentReconciliationNotCollected"
import type { PaymentReconciliationNotMatched } from "#generated/platform/PaymentReconciliationNotMatched"

export type PaymentReconciliation =
	| PaymentReconciliationIncomparable
	| PaymentReconciliationMatched
	| PaymentReconciliationNotCollected
	| PaymentReconciliationNotMatched
