package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 웹훅 내역이 존재하지 않는 경우 */
@Serializable
@SerialName("WEBHOOK_NOT_FOUND")
@ConsistentCopyVisibility
public data class WebhookNotFoundError internal constructor(
  val message: String? = null,
) : ResendWebhookError
