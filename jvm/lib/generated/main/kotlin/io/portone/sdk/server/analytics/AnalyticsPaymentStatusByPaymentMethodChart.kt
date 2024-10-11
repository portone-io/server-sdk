package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentStatusByPaymentMethodChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제 수단 별 결제 상태 차트 정보 */
@Serializable
public data class AnalyticsPaymentStatusByPaymentMethodChart(
  val stats: Array<AnalyticsPaymentStatusByPaymentMethodChartStat>,
)
