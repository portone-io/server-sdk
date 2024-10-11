package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제 현황 차트 정보 */
@Serializable
public data class AnalyticsPaymentChart(
  val stats: List<AnalyticsPaymentChartStat>,
)
