import type { PlatformManualTransferSummary } from "./../../platform/transfer/PlatformManualTransferSummary"
import type { PlatformOrderCancelTransferSummary } from "./../../platform/transfer/PlatformOrderCancelTransferSummary"
import type { PlatformOrderTransferSummary } from "./../../platform/transfer/PlatformOrderTransferSummary"

export type PlatformTransferSummary =
	| PlatformManualTransferSummary
	| PlatformOrderTransferSummary
	| PlatformOrderCancelTransferSummary
	| { readonly type: unique symbol }
