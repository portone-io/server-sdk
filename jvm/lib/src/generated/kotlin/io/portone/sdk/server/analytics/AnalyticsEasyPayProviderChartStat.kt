package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.EasyPayProvider
import java.time.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 간편결제사별 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsEasyPayProviderChartStat(
  /** 시점 */
  val timestamp: Instant,
  /** 간편결제사 */
  val easyPayProvider: EasyPayProvider,
  /** 결제금액 */
  val amount: Long,
  /** 결제 건수 */
  val count: Long,
)
