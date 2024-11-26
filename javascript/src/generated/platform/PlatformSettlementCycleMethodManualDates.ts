import type { MonthDay } from "./../platform/MonthDay"
/** 정해진 날짜(월, 일)에 정산 */
export type PlatformSettlementCycleMethodManualDates = {
	type: "MANUAL_DATES"
	/** 월 및 일자 정보 */
	dates: MonthDay[]
}
