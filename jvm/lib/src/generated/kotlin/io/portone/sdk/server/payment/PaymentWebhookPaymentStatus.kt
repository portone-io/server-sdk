package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 웹훅 발송 시 결제 건 상태 */
@Serializable(PaymentWebhookPaymentStatusSerializer::class)
public sealed interface PaymentWebhookPaymentStatus {
  public val value: String
  public data object Ready : PaymentWebhookPaymentStatus {
    override val value: String = "READY"
  }
  public data object VirtualAccountIssued : PaymentWebhookPaymentStatus {
    override val value: String = "VIRTUAL_ACCOUNT_ISSUED"
  }
  public data object Paid : PaymentWebhookPaymentStatus {
    override val value: String = "PAID"
  }
  public data object Failed : PaymentWebhookPaymentStatus {
    override val value: String = "FAILED"
  }
  public data object PartialCancelled : PaymentWebhookPaymentStatus {
    override val value: String = "PARTIAL_CANCELLED"
  }
  public data object Cancelled : PaymentWebhookPaymentStatus {
    override val value: String = "CANCELLED"
  }
  public data object PayPending : PaymentWebhookPaymentStatus {
    override val value: String = "PAY_PENDING"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookPaymentStatus
}


private object PaymentWebhookPaymentStatusSerializer : KSerializer<PaymentWebhookPaymentStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentWebhookPaymentStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentWebhookPaymentStatus {
    val value = decoder.decodeString()
    return when (value) {
      "READY" -> PaymentWebhookPaymentStatus.Ready
      "VIRTUAL_ACCOUNT_ISSUED" -> PaymentWebhookPaymentStatus.VirtualAccountIssued
      "PAID" -> PaymentWebhookPaymentStatus.Paid
      "FAILED" -> PaymentWebhookPaymentStatus.Failed
      "PARTIAL_CANCELLED" -> PaymentWebhookPaymentStatus.PartialCancelled
      "CANCELLED" -> PaymentWebhookPaymentStatus.Cancelled
      "PAY_PENDING" -> PaymentWebhookPaymentStatus.PayPending
      else -> PaymentWebhookPaymentStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentWebhookPaymentStatus) = encoder.encodeString(value.value)
}
