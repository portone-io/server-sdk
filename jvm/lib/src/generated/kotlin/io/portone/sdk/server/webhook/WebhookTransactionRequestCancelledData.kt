package io.portone.sdk.server.webhook

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class WebhookTransactionRequestCancelledData(
  /** 고객사에서 채번한 결제 건의 고유 주문 번호입니다. */
  val paymentId: String,
  /** 포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다. */
  val transactionId: String,
  /** 포트원에서 채번한 결제건의 취소 고유 번호입니다. `type` 이 `Transaction.PartialCancelled` 혹은 `Transaction.Cancelled` 일 때 존재합니다. */
  val cancellationId: String,
)
