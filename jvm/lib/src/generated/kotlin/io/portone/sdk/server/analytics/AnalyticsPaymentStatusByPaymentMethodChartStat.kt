package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PaymentMethodType
import io.portone.sdk.server.common.PaymentStatus
import kotlinx.serialization.Serializable

/** 각 결제수단, 상태 별 건수와 금액을 나타냅니다. */
@Serializable
public data class AnalyticsPaymentStatusByPaymentMethodChartStat(
  /** 결제 건 상태 */
  val paymentStatus: PaymentStatus,
  /** 거래액 */
  val amount: Long,
  /** 거래 건수 */
  val count: Long,
  /** 결제수단 */
  val paymentMethod: PaymentMethodType? = null,
)
