package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 웹훅 발송 시 결제 건 상태 */
@Serializable
public sealed interface PaymentWebhookPaymentStatus {
  public val value: String
  @SerialName("READY")
  public data object Ready : PaymentWebhookPaymentStatus {
    override val value: String = "READY"
  }
  @SerialName("VIRTUAL_ACCOUNT_ISSUED")
  public data object VirtualAccountIssued : PaymentWebhookPaymentStatus {
    override val value: String = "VIRTUAL_ACCOUNT_ISSUED"
  }
  @SerialName("PAID")
  public data object Paid : PaymentWebhookPaymentStatus {
    override val value: String = "PAID"
  }
  @SerialName("FAILED")
  public data object Failed : PaymentWebhookPaymentStatus {
    override val value: String = "FAILED"
  }
  @SerialName("PARTIAL_CANCELLED")
  public data object PartialCancelled : PaymentWebhookPaymentStatus {
    override val value: String = "PARTIAL_CANCELLED"
  }
  @SerialName("CANCELLED")
  public data object Cancelled : PaymentWebhookPaymentStatus {
    override val value: String = "CANCELLED"
  }
  @SerialName("PAY_PENDING")
  public data object PayPending : PaymentWebhookPaymentStatus {
    override val value: String = "PAY_PENDING"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookPaymentStatus
}
