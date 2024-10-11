package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.CardCompany
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 카드사 별 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsCardCompanyChartStat(
  /** 시점 */
  val timestamp: Instant,
  /** 카드사 */
  val cardCompany: CardCompany,
  /** 결제금액 */
  val amount: Long,
  /** 결제 건수 */
  val count: Long,
)
