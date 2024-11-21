package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 웹훅 전송 상태 */
@Serializable
public sealed interface PaymentWebhookStatus {
  public val value: String
  @SerialName("SUCCEEDED")
  public data object Succeeded : PaymentWebhookStatus {
    override val value: String = "SUCCEEDED"
  }
  @SerialName("FAILED_NOT_OK_RESPONSE")
  public data object FailedNotOkResponse : PaymentWebhookStatus {
    override val value: String = "FAILED_NOT_OK_RESPONSE"
  }
  @SerialName("FAILED_UNEXPECTED_ERROR")
  public data object FailedUnexpectedError : PaymentWebhookStatus {
    override val value: String = "FAILED_UNEXPECTED_ERROR"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookStatus
}
