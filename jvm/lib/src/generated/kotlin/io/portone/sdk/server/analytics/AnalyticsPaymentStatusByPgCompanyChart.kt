package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentStatusByPgCompanyChartStat
import kotlinx.serialization.Serializable

/** 고객사의 PG사 별 결제 상태 차트 정보 */
@Serializable
public data class AnalyticsPaymentStatusByPgCompanyChart(
  val stats: List<AnalyticsPaymentStatusByPgCompanyChartStat>,
)
