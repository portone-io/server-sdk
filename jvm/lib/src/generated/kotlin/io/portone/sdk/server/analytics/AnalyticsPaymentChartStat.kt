package io.portone.sdk.server.analytics

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 거래 건 수와 금액을 나타냅니다. */
@Serializable
public data class AnalyticsPaymentChartStat(
  /** 시점 */
  val timestamp: @Serializable(InstantSerializer::class) Instant,
  /** 거래액 */
  val amount: Long,
  /** 거래 건수 */
  val count: Long,
)
