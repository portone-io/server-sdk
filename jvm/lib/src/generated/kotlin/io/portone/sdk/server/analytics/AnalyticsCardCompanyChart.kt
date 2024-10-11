package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsCardCompanyChartRemainderStat
import io.portone.sdk.server.analytics.AnalyticsCardCompanyChartStat
import io.portone.sdk.server.analytics.AnalyticsCardCompanyChartSummary
import kotlinx.serialization.Serializable

/** 고객사의 카드사별 결제 현황 조회 응답 */
@Serializable
public data class AnalyticsCardCompanyChart(
  val stats: List<AnalyticsCardCompanyChartStat>,
  val remainderStats: List<AnalyticsCardCompanyChartRemainderStat>,
  val summary: AnalyticsCardCompanyChartSummary,
)
