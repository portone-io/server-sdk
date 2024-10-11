package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PgCompany
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 특정 시점의 결제대행사 별 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsPgCompanyTrendChartStat(
  /** 시점 */
  val timestamp: Instant,
  /** 결제대행사 */
  val pgCompany: PgCompany,
  /** 결제금액 */
  val amount: Long,
  /** 결제 건수 */
  val count: Long,
)
