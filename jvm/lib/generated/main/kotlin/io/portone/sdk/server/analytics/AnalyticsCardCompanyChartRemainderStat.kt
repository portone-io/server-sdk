package io.portone.sdk.server.analytics

import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 나머지 카드사들의 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsCardCompanyChartRemainderStat(
  /** 시점 */
  val timestamp: Instant,
  /** 결제금액 */
  val amount: Long,
  /** 결제 건수 */
  val count: Long,
)
