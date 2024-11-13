import type { PlatformTransferSummaryExternalPayment } from "./../../platform/transfer/PlatformTransferSummaryExternalPayment"
import type { PlatformTransferSummaryPortOnePayment } from "./../../platform/transfer/PlatformTransferSummaryPortOnePayment"

export type PlatformTransferSummaryPayment =
	| PlatformTransferSummaryExternalPayment
	| PlatformTransferSummaryPortOnePayment
	| { readonly type: unique symbol }
