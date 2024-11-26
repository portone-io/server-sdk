package io.portone.sdk.server.webhook

import io.portone.sdk.server.webhook.WebhookTransactionData
import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제(예약 결제 포함)가 승인되었을 때 이벤트의 실제 세부 내용입니다. (모든 결제 수단) */
@Serializable
@ConsistentCopyVisibility
public data class WebhookTransactionDataPaid internal constructor(
  /** 고객사에서 채번한 결제 건의 고유 주문 번호입니다. */
  override val paymentId: String,
  /** 포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다. */
  override val transactionId: String,
) : WebhookTransactionData
