package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PaymentStatus
import kotlinx.serialization.Serializable

/** 각 상태의 건수와 금액, 사분위수를 나타냅니다. */
@Serializable
public data class AnalyticsPaymentStatusChartStat(
  /** 결제 건 상태 */
  val paymentStatus: PaymentStatus,
  /** 거래액 */
  val amount: Long,
  /** 거래 건수 */
  val count: Long,
  /** 해당 상태 비율 */
  val averageRatio: Long,
  /** 1 사분위수 */
  val firstQuantile: Long,
  /** 중앙값 */
  val median: Long,
  /** 3 사분위수 */
  val thirdQuantile: Long,
)
