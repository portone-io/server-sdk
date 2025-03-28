package io.portone.sdk.server.webhook

import io.portone.sdk.server.webhook.WebhookTransactionData
import kotlin.String
import kotlinx.serialization.Serializable

/** 결제 승인 대기 상태가 되었을 때 이벤트의 실제 세부 내용입니다. (해외 결제시 발생 가능) */
@Serializable
public data class WebhookTransactionDataPayPending internal constructor(
  /** 고객사에서 채번한 결제 건의 고유 주문 번호입니다. */
  override val paymentId: String,
  /** 웹훅을 트리거한 상점의 아이디입니다. */
  override val storeId: String,
  /** 포트원에서 채번한 고유 거래 번호입니다. 한 결제 건에 여러 시도가 있을 경우 `transactionId` 가 달라질 수 있습니다. */
  override val transactionId: String,
) : WebhookTransactionData
