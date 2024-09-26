import type { DayOfWeek } from "#generated/common/DayOfWeek"

/** 매주 정해진 요일에 정산 */
export type PlatformSettlementCycleMethodWeekly = {
	type: "WEEKLY"
	/** 요일 */
	daysOfWeek: DayOfWeek[]
}
