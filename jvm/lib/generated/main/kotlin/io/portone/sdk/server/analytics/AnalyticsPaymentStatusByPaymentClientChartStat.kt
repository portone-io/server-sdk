package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.PaymentClientType
import io.portone.sdk.server.common.PaymentStatus
import kotlinx.serialization.Serializable

/** 고객사의 결제 환경 별 결제 상태 차트 정보 */
@Serializable
public data class AnalyticsPaymentStatusByPaymentClientChartStat(
  /** 결제가 발생한 클라이언트 환경 */
  val paymentClientType: PaymentClientType,
  /** 결제 건 상태 */
  val paymentStatus: PaymentStatus,
  /** 거래액 */
  val amount: Long,
  /** 거래 건수 */
  val count: Long,
)
