import type { AnalyticsTimeGranularityDay } from "#generated/analytics/AnalyticsTimeGranularityDay"
import type { AnalyticsTimeGranularityHour } from "#generated/analytics/AnalyticsTimeGranularityHour"
import type { AnalyticsTimeGranularityMinute } from "#generated/analytics/AnalyticsTimeGranularityMinute"
import type { AnalyticsTimeGranularityMonth } from "#generated/analytics/AnalyticsTimeGranularityMonth"
import type { AnalyticsTimeGranularityWeek } from "#generated/analytics/AnalyticsTimeGranularityWeek"

/**
 * 조회 시간 단위
 *
 * 하나의 단위 필드만 선택하여 입력합니다.
 */
export type AnalyticsTimeGranularity = {
	minute?: AnalyticsTimeGranularityMinute
	hour?: AnalyticsTimeGranularityHour
	day?: AnalyticsTimeGranularityDay
	week?: AnalyticsTimeGranularityWeek
	month?: AnalyticsTimeGranularityMonth
}
