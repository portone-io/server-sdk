package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsEasyPayChartStat
import kotlinx.serialization.Serializable

/** 고객사의 간편결제 현황 차트 정보 */
@Serializable
public data class AnalyticsEasyPayChart(
  val stats: List<AnalyticsEasyPayChartStat>,
)
