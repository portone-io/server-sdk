import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PlatformManualTransferSummary } from "./../../platform/transfer/PlatformManualTransferSummary"
import type { PlatformOrderCancelTransferSummary } from "./../../platform/transfer/PlatformOrderCancelTransferSummary"
import type { PlatformOrderTransferSummary } from "./../../platform/transfer/PlatformOrderTransferSummary"
export type PlatformTransferSummary =
	| PlatformManualTransferSummary
	| PlatformOrderTransferSummary
	| PlatformOrderCancelTransferSummary
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformTransferSummary(entity: PlatformTransferSummary): entity is { readonly type: Unrecognized } {
	return entity.type !== "MANUAL"
		&& entity.type !== "ORDER"
		&& entity.type !== "ORDER_CANCEL"
}
