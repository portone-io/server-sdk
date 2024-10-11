package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsAverageAmountChartStat
import io.portone.sdk.server.analytics.AnalyticsAverageAmountChartSummary
import kotlinx.serialization.Serializable

/** 고객사의 평균 거래액 현황 조회 응답 */
@Serializable
public data class AnalyticsAverageAmountChart(
  val stats: List<AnalyticsAverageAmountChartStat>,
  val summary: AnalyticsAverageAmountChartSummary,
)
