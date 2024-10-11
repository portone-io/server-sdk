package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsEasyPayProviderChartRemainderStat
import io.portone.sdk.server.analytics.AnalyticsEasyPayProviderChartStat
import io.portone.sdk.server.analytics.AnalyticsEasyPayProviderChartSummary
import kotlinx.serialization.Serializable

/** 고객사의 간편결제사별 결제 현황 차트 정보 */
@Serializable
public data class AnalyticsEasyPayProviderChart(
  val stats: Array<AnalyticsEasyPayProviderChartStat>,
  val remainderStats: Array<AnalyticsEasyPayProviderChartRemainderStat>,
  val summary: AnalyticsEasyPayProviderChartSummary,
)
