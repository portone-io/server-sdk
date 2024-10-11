package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PgCompany
import kotlinx.serialization.Serializable

/** 결제대행사별 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsPgCompanyChartStat(
  /** 결제대행사 */
  val pgCompany: PgCompany,
  /** 결제대행사별 결제금액 */
  val amount: Long,
  /** 결제대행사별 결제 건수 */
  val count: Long,
)
