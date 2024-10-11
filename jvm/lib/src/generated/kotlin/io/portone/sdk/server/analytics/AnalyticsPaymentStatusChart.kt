package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentStatusChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제 상태 차트 정보 */
@Serializable
public data class AnalyticsPaymentStatusChart(
  val stats: Array<AnalyticsPaymentStatusChartStat>,
)
