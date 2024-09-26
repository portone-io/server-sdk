import type { AnalyticsEasyPayProviderChartRemainderStat } from "#generated/analytics/AnalyticsEasyPayProviderChartRemainderStat"
import type { AnalyticsEasyPayProviderChartStat } from "#generated/analytics/AnalyticsEasyPayProviderChartStat"
import type { AnalyticsEasyPayProviderChartSummary } from "#generated/analytics/AnalyticsEasyPayProviderChartSummary"

/** 고객사의 간편결제사별 결제 현황 차트 정보 */
export type AnalyticsEasyPayProviderChart = {
	stats: AnalyticsEasyPayProviderChartStat[]
	remainderStats: AnalyticsEasyPayProviderChartRemainderStat[]
	summary: AnalyticsEasyPayProviderChartSummary
}
