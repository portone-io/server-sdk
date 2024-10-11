package io.portone.sdk.server.analytics

import java.time.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 간편결제 거래 건수와 금액을 나타냅니다. */
@Serializable
public data class AnalyticsEasyPayChartStat(
  /** 시점 */
  val timestamp: Instant,
  /** 거래액 */
  val amount: Long,
  /** 거래 건수 */
  val count: Long,
)
