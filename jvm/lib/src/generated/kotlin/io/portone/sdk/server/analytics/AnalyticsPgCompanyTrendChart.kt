package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPgCompanyTrendChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제대행사별 거래 추이 차트 정보 */
@Serializable
public data class AnalyticsPgCompanyTrendChart(
  val stats: Array<AnalyticsPgCompanyTrendChartStat>,
)
