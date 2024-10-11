package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PaymentStatus
import io.portone.sdk.server.common.PgCompany
import kotlinx.serialization.Serializable

/** 각 상태의 건수와 금액, 사분위수를 나타냅니다. */
@Serializable
public data class AnalyticsPaymentStatusByPgCompanyChartStat(
  /** PG사 */
  val pgCompany: PgCompany,
  /** 결제 건 상태 */
  val paymentStatus: PaymentStatus,
  /** 거래액 */
  val amount: Long,
  /** 거래 건수 */
  val count: Long,
)
