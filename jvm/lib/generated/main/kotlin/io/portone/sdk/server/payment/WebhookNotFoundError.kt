package io.portone.sdk.server.payment

import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 웹훅 내역이 존재하지 않는 경우 */
@Serializable
@SerialName("WEBHOOK_NOT_FOUND")
public data class WebhookNotFoundError(
  override val message: String? = null,
): ResendWebhookError,
