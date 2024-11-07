import type { PlatformSettlementCycleMethodDaily } from "./../platform/PlatformSettlementCycleMethodDaily"
import type { PlatformSettlementCycleMethodManualDates } from "./../platform/PlatformSettlementCycleMethodManualDates"
import type { PlatformSettlementCycleMethodMonthly } from "./../platform/PlatformSettlementCycleMethodMonthly"
import type { PlatformSettlementCycleMethodWeekly } from "./../platform/PlatformSettlementCycleMethodWeekly"

/** 플랫폼 정산 주기 계산 방식 */
export type PlatformSettlementCycleMethod =
	/** 매일 정산 */
	| PlatformSettlementCycleMethodDaily
	/** 정해진 날짜(월, 일)에 정산 */
	| PlatformSettlementCycleMethodManualDates
	/** 매월 정해진 날(일)에 정산 */
	| PlatformSettlementCycleMethodMonthly
	/** 매주 정해진 요일에 정산 */
	| PlatformSettlementCycleMethodWeekly
