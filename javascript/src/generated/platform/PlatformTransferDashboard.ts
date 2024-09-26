import type { DateRange } from "#generated/platform/DateRange"

export type PlatformTransferDashboard = {
	/** (int64) */
	totalSettlementAmount: number
	/** (int64) */
	totalSettlementFeeAmount: number
	/** (int64) */
	totalOrderAmount: number
	settlementStartDateRange?: DateRange
}
