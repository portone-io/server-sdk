import type { AnalyticsCardCompanyChartRemainderStat } from "#generated/analytics/AnalyticsCardCompanyChartRemainderStat"
import type { AnalyticsCardCompanyChartStat } from "#generated/analytics/AnalyticsCardCompanyChartStat"
import type { AnalyticsCardCompanyChartSummary } from "#generated/analytics/AnalyticsCardCompanyChartSummary"

/** 고객사의 카드사별 결제 현황 조회 응답 */
export type AnalyticsCardCompanyChart = {
	stats: AnalyticsCardCompanyChartStat[]
	remainderStats: AnalyticsCardCompanyChartRemainderStat[]
	summary: AnalyticsCardCompanyChartSummary
}
