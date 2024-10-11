package io.portone.sdk.server.analytics

import java.time.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 건별 평균 거래액, 고객 당 평균 거래액을 나타냅니다. */
@Serializable
public data class AnalyticsAverageAmountChartStat(
  /** 시점 */
  val timestamp: Instant,
  /** 건별 평균 거래액 */
  val paymentAverageAmount: Long,
  /** 고객 당 평균 거래액 */
  val customerAverageAmount: Long,
)
