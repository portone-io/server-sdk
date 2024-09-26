import type { PlatformSettlementCycleMethodDailyInput } from "#generated/platform/PlatformSettlementCycleMethodDailyInput"
import type { PlatformSettlementCycleMethodManualDatesInput } from "#generated/platform/PlatformSettlementCycleMethodManualDatesInput"
import type { PlatformSettlementCycleMethodMonthlyInput } from "#generated/platform/PlatformSettlementCycleMethodMonthlyInput"
import type { PlatformSettlementCycleMethodWeeklyInput } from "#generated/platform/PlatformSettlementCycleMethodWeeklyInput"

/**
 * 플랫폼 정산 주기 계산 방식 입력 정보
 *
 * 하나의 하위 필드에만 값을 명시하여 요청합니다.
 */
export type PlatformSettlementCycleMethodInput = {
	/** 매일 정산 */
	daily?: PlatformSettlementCycleMethodDailyInput
	/** 매주 정해진 요일에 정산 */
	weekly?: PlatformSettlementCycleMethodWeeklyInput
	/** 매월 정해진 날(일)에 정산 */
	monthly?: PlatformSettlementCycleMethodMonthlyInput
	/** 정해진 날짜(월, 일)에 정산 */
	manualDates?: PlatformSettlementCycleMethodManualDatesInput
}
