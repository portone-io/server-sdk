package io.portone.sdk.server.analytics

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 나머지 간편결제사들의 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsEasyPayProviderChartRemainderStat(
  /** 시점 */
  val timestamp: @Serializable(InstantSerializer::class) Instant,
  /** 결제금액 */
  val amount: Long,
  /** 결제 건수 */
  val count: Long,
)
