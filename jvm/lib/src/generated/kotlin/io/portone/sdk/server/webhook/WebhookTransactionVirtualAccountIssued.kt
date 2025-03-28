package io.portone.sdk.server.webhook

import io.portone.sdk.server.serializers.InstantSerializer
import io.portone.sdk.server.webhook.WebhookTransaction
import io.portone.sdk.server.webhook.WebhookTransactionDataVirtualAccountIssued
import java.time.Instant
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 가상계좌가 발급되었을 때 */
@Serializable
@SerialName("Transaction.VirtualAccountIssued")
public data class WebhookTransactionVirtualAccountIssued internal constructor(
  /** 해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다. */
  override val timestamp: @Serializable(InstantSerializer::class) Instant,
  /** 가상계좌가 발급되었을 때 이벤트의 실제 세부 내용입니다. */
  override val data: WebhookTransactionDataVirtualAccountIssued,
) : WebhookTransaction
