package io.portone.sdk.server.webhook

import io.portone.sdk.server.serializers.InstantSerializer
import io.portone.sdk.server.webhook.Webhook
import io.portone.sdk.server.webhook.WebhookBillingKeyData
import java.time.Instant
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 빌링키 발급 관련 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface WebhookBillingKey : Webhook {
  /** 해당 웹훅을 트리거한 이벤트의 발생 시각(RFC 3339 형식)입니다. 고객사 서버가 웹훅을 수신하는 데 실패하여 재시도가 일어나도 이 값은 동일하게 유지됩니다. */
  public val timestamp: @Serializable(InstantSerializer::class) Instant
  /** 웹훅을 트리거한 이벤트의 실제 세부 내용입니다. */
  public val data: WebhookBillingKeyData
}
