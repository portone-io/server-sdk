package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 에스크로 상태 */
@Serializable(PaymentFilterInputEscrowStatusSerializer::class)
public sealed interface PaymentFilterInputEscrowStatus {
  public val value: String
  @Serializable(RegisteredSerializer::class)
  public data object Registered : PaymentFilterInputEscrowStatus {
    override val value: String = "REGISTERED"
  }
  private object RegisteredSerializer : KSerializer<Registered> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Registered::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Registered = decoder.decodeString().let {
      if (it != "REGISTERED") {
        throw SerializationException(it)
      } else {
        return Registered
      }
    }
    override fun serialize(encoder: Encoder, value: Registered) = encoder.encodeString(value.value)
  }
  @Serializable(DeliveredSerializer::class)
  public data object Delivered : PaymentFilterInputEscrowStatus {
    override val value: String = "DELIVERED"
  }
  private object DeliveredSerializer : KSerializer<Delivered> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Delivered::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Delivered = decoder.decodeString().let {
      if (it != "DELIVERED") {
        throw SerializationException(it)
      } else {
        return Delivered
      }
    }
    override fun serialize(encoder: Encoder, value: Delivered) = encoder.encodeString(value.value)
  }
  @Serializable(ConfirmedSerializer::class)
  public data object Confirmed : PaymentFilterInputEscrowStatus {
    override val value: String = "CONFIRMED"
  }
  private object ConfirmedSerializer : KSerializer<Confirmed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Confirmed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Confirmed = decoder.decodeString().let {
      if (it != "CONFIRMED") {
        throw SerializationException(it)
      } else {
        return Confirmed
      }
    }
    override fun serialize(encoder: Encoder, value: Confirmed) = encoder.encodeString(value.value)
  }
  @Serializable(RejectedSerializer::class)
  public data object Rejected : PaymentFilterInputEscrowStatus {
    override val value: String = "REJECTED"
  }
  private object RejectedSerializer : KSerializer<Rejected> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Rejected::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Rejected = decoder.decodeString().let {
      if (it != "REJECTED") {
        throw SerializationException(it)
      } else {
        return Rejected
      }
    }
    override fun serialize(encoder: Encoder, value: Rejected) = encoder.encodeString(value.value)
  }
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PaymentFilterInputEscrowStatus {
    override val value: String = "CANCELLED"
  }
  private object CancelledSerializer : KSerializer<Cancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cancelled = decoder.decodeString().let {
      if (it != "CANCELLED") {
        throw SerializationException(it)
      } else {
        return Cancelled
      }
    }
    override fun serialize(encoder: Encoder, value: Cancelled) = encoder.encodeString(value.value)
  }
  @Serializable(RejectConfirmedSerializer::class)
  public data object RejectConfirmed : PaymentFilterInputEscrowStatus {
    override val value: String = "REJECT_CONFIRMED"
  }
  private object RejectConfirmedSerializer : KSerializer<RejectConfirmed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(RejectConfirmed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): RejectConfirmed = decoder.decodeString().let {
      if (it != "REJECT_CONFIRMED") {
        throw SerializationException(it)
      } else {
        return RejectConfirmed
      }
    }
    override fun serialize(encoder: Encoder, value: RejectConfirmed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentFilterInputEscrowStatus
}


private object PaymentFilterInputEscrowStatusSerializer : KSerializer<PaymentFilterInputEscrowStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentFilterInputEscrowStatus::class.java.name, PrimitiveKind.STRING)
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
