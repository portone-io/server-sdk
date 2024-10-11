package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentMethodChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제수단 현황 차트 정보 */
@Serializable
public data class AnalyticsPaymentMethodChart(
  val stats: Array<AnalyticsPaymentMethodChartStat>,
)
