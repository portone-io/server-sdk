package io.portone.sdk.server.webhook

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class WebhookTransactionRequestPayPendingData(
  /** 고객사에서 채번한 결제 건의 고유 주문 번호입니다. */
  val paymentId: String,
  /** 포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다. */
  val transactionId: String,
)
