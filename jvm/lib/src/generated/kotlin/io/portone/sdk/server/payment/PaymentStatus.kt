package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 건 상태 */
@Serializable(PaymentStatusSerializer::class)
public sealed interface PaymentStatus {
  public val value: String
  public data object Ready : PaymentStatus {
    override val value: String = "READY"
  }
  public data object Pending : PaymentStatus {
    override val value: String = "PENDING"
  }
  public data object VirtualAccountIssued : PaymentStatus {
    override val value: String = "VIRTUAL_ACCOUNT_ISSUED"
  }
  public data object Paid : PaymentStatus {
    override val value: String = "PAID"
  }
  public data object Failed : PaymentStatus {
    override val value: String = "FAILED"
  }
  public data object PartialCancelled : PaymentStatus {
    override val value: String = "PARTIAL_CANCELLED"
  }
  public data object Cancelled : PaymentStatus {
    override val value: String = "CANCELLED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentStatus
}


private object PaymentStatusSerializer : KSerializer<PaymentStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentStatus {
    val value = decoder.decodeString()
    return when (value) {
      "READY" -> PaymentStatus.Ready
      "PENDING" -> PaymentStatus.Pending
      "VIRTUAL_ACCOUNT_ISSUED" -> PaymentStatus.VirtualAccountIssued
      "PAID" -> PaymentStatus.Paid
      "FAILED" -> PaymentStatus.Failed
      "PARTIAL_CANCELLED" -> PaymentStatus.PartialCancelled
      "CANCELLED" -> PaymentStatus.Cancelled
      else -> PaymentStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentStatus) = encoder.encodeString(value.value)
}
