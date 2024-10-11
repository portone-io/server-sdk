package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsCardChartStat
import kotlinx.serialization.Serializable

/** 고객사의 카드결제 현황 차트 정보 */
@Serializable
public data class AnalyticsCardChart(
  val stats: Array<AnalyticsCardChartStat>,
)
