package io.portone.sdk.server.errors

import kotlin.ConsistentCopyVisibility
import kotlin.String
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 동일한 webhook id에 대한 수동 재시도 횟수가 최대에 도달한 경우 */
@Serializable
@SerialName("MAX_WEBHOOK_RETRY_COUNT_REACHED")
@ConsistentCopyVisibility
public data class MaxWebhookRetryCountReachedError internal constructor(
  val message: String? = null,
) : ResendWebhookError
