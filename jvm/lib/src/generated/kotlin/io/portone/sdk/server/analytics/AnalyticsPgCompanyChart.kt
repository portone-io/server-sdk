package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPgCompanyChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제대행사 현황 차트 정보 */
@Serializable
public data class AnalyticsPgCompanyChart(
  val stats: Array<AnalyticsPgCompanyChartStat>,
)
