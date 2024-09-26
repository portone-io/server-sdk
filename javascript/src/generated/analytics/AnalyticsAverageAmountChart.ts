import type { AnalyticsAverageAmountChartStat } from "#generated/analytics/AnalyticsAverageAmountChartStat"
import type { AnalyticsAverageAmountChartSummary } from "#generated/analytics/AnalyticsAverageAmountChartSummary"

/** 고객사의 평균 거래액 현황 조회 응답 */
export type AnalyticsAverageAmountChart = {
	stats: AnalyticsAverageAmountChartStat[]
	summary: AnalyticsAverageAmountChartSummary
}
