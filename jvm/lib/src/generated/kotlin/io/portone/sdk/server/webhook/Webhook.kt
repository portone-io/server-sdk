package io.portone.sdk.server.webhook

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

/** 2024-04-25 버전의 웹훅 형식 */
@Serializable
@JsonClassDiscriminator("type")
public sealed interface Webhook {
  @Serializable
  public data object Unrecognized : Webhook
}
