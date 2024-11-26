import type { Unrecognized } from "./../../../utils/unrecognized"
import type { PlatformTransferSummaryExternalPayment } from "./../../platform/transfer/PlatformTransferSummaryExternalPayment"
import type { PlatformTransferSummaryPortOnePayment } from "./../../platform/transfer/PlatformTransferSummaryPortOnePayment"
export type PlatformTransferSummaryPayment =
	| PlatformTransferSummaryExternalPayment
	| PlatformTransferSummaryPortOnePayment
	| { readonly type: Unrecognized }

export function isUnrecognizedPlatformTransferSummaryPayment(entity: PlatformTransferSummaryPayment): entity is { readonly type: Unrecognized } {
	return entity.type !== "EXTERNAL"
		&& entity.type !== "PORT_ONE"
}
