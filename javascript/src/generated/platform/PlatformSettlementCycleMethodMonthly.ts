/** 매월 정해진 날(일)에 정산 */
export type PlatformSettlementCycleMethodMonthly = {
	type: "MONTHLY"
	daysOfMonth: number[]
}
