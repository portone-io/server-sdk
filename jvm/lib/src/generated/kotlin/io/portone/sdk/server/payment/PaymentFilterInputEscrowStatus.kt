package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 에스크로 상태 */
@Serializable(PaymentFilterInputEscrowStatusSerializer::class)
public sealed interface PaymentFilterInputEscrowStatus {
  public val value: String
  public data object Registered : PaymentFilterInputEscrowStatus {
    override val value: String = "REGISTERED"
  }
  public data object Delivered : PaymentFilterInputEscrowStatus {
    override val value: String = "DELIVERED"
  }
  public data object Confirmed : PaymentFilterInputEscrowStatus {
    override val value: String = "CONFIRMED"
  }
  public data object Rejected : PaymentFilterInputEscrowStatus {
    override val value: String = "REJECTED"
  }
  public data object Cancelled : PaymentFilterInputEscrowStatus {
    override val value: String = "CANCELLED"
  }
  public data object RejectConfirmed : PaymentFilterInputEscrowStatus {
    override val value: String = "REJECT_CONFIRMED"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentFilterInputEscrowStatus
}


private object PaymentFilterInputEscrowStatusSerializer : KSerializer<PaymentFilterInputEscrowStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentFilterInputEscrowStatus::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentFilterInputEscrowStatus {
    val value = decoder.decodeString()
    return when (value) {
      "REGISTERED" -> PaymentFilterInputEscrowStatus.Registered
      "DELIVERED" -> PaymentFilterInputEscrowStatus.Delivered
      "CONFIRMED" -> PaymentFilterInputEscrowStatus.Confirmed
      "REJECTED" -> PaymentFilterInputEscrowStatus.Rejected
      "CANCELLED" -> PaymentFilterInputEscrowStatus.Cancelled
      "REJECT_CONFIRMED" -> PaymentFilterInputEscrowStatus.RejectConfirmed
      else -> PaymentFilterInputEscrowStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentFilterInputEscrowStatus) = encoder.encodeString(value.value)
}
