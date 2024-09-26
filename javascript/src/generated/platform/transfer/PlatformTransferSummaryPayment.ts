import type { PlatformTransferSummaryExternalPayment } from "#generated/platform/transfer/PlatformTransferSummaryExternalPayment"
import type { PlatformTransferSummaryPortOnePayment } from "#generated/platform/transfer/PlatformTransferSummaryPortOnePayment"

export type PlatformTransferSummaryPayment =
	| PlatformTransferSummaryExternalPayment
	| PlatformTransferSummaryPortOnePayment
