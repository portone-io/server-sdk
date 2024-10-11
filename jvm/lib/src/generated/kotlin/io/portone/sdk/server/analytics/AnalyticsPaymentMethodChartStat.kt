package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PaymentMethodType
import kotlinx.serialization.Serializable

/** 결제수단별 결제금액, 결제 건수를 나타냅니다. */
@Serializable
public data class AnalyticsPaymentMethodChartStat(
  /** 결제수단별 결제금액 */
  val amount: Long,
  /** 결제수단별 결제 건수 */
  val count: Long,
  /** 결제수단 */
  val paymentMethod: PaymentMethodType? = null,
)
