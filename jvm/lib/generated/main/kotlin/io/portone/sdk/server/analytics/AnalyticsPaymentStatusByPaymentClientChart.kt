package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentStatusByPaymentClientChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제 환경 별 결제 상태 차트 정보 */
@Serializable
public data class AnalyticsPaymentStatusByPaymentClientChart(
  val stats: Array<AnalyticsPaymentStatusByPaymentClientChartStat>,
)