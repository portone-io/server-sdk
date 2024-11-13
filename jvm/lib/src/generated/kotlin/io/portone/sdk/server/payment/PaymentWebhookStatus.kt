package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 웹훅 전송 상태 */
@Serializable
public sealed class PaymentWebhookStatus {
  @SerialName("SUCCEEDED")
  public data object Succeeded : PaymentWebhookStatus()
  @SerialName("FAILED_NOT_OK_RESPONSE")
  public data object FailedNotOkResponse : PaymentWebhookStatus()
  @SerialName("FAILED_UNEXPECTED_ERROR")
  public data object FailedUnexpectedError : PaymentWebhookStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentWebhookStatus()
}
