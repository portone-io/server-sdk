import type { PlatformManualTransferSummary } from "#generated/platform/transfer/PlatformManualTransferSummary"
import type { PlatformOrderCancelTransferSummary } from "#generated/platform/transfer/PlatformOrderCancelTransferSummary"
import type { PlatformOrderTransferSummary } from "#generated/platform/transfer/PlatformOrderTransferSummary"

export type PlatformTransferSummary =
	| PlatformManualTransferSummary
	| PlatformOrderTransferSummary
	| PlatformOrderCancelTransferSummary
