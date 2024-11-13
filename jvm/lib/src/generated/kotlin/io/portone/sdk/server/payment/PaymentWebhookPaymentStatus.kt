package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 웹훅 발송 시 결제 건 상태 */
@Serializable
public sealed class PaymentWebhookPaymentStatus {
  @SerialName("READY")
  public data object Ready : PaymentWebhookPaymentStatus()
  @SerialName("VIRTUAL_ACCOUNT_ISSUED")
  public data object VirtualAccountIssued : PaymentWebhookPaymentStatus()
  @SerialName("PAID")
  public data object Paid : PaymentWebhookPaymentStatus()
  @SerialName("FAILED")
  public data object Failed : PaymentWebhookPaymentStatus()
  @SerialName("PARTIAL_CANCELLED")
  public data object PartialCancelled : PaymentWebhookPaymentStatus()
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentWebhookPaymentStatus()
  @SerialName("PAY_PENDING")
  public data object PayPending : PaymentWebhookPaymentStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PaymentWebhookPaymentStatus()
}
