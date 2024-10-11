package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 전체 구간의 건별 평균 거래액, 고객 당 평균 거래액을 나타냅니다. */
@Serializable
public data class AnalyticsAverageAmountChartSummary(
  /** 건별 평균 거래액 */
  val paymentAverageAmount: Long,
  /** 고객 당 평균 거래액 */
  val customerAverageAmount: Long,
)
