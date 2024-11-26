package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제 건 상태 */
@Serializable(PaymentStatusSerializer::class)
public sealed interface PaymentStatus {
  public val value: String
  @Serializable(ReadySerializer::class)
  public data object Ready : PaymentStatus {
    override val value: String = "READY"
  }
  private object ReadySerializer : KSerializer<Ready> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ready::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ready = decoder.decodeString().let {
      if (it != "READY") {
        throw SerializationException(it)
      } else {
        return Ready
      }
    }
    override fun serialize(encoder: Encoder, value: Ready) = encoder.encodeString(value.value)
  }
  @Serializable(PendingSerializer::class)
  public data object Pending : PaymentStatus {
    override val value: String = "PENDING"
  }
  private object PendingSerializer : KSerializer<Pending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pending = decoder.decodeString().let {
      if (it != "PENDING") {
        throw SerializationException(it)
      } else {
        return Pending
      }
    }
    override fun serialize(encoder: Encoder, value: Pending) = encoder.encodeString(value.value)
  }
  @Serializable(VirtualAccountIssuedSerializer::class)
  public data object VirtualAccountIssued : PaymentStatus {
    override val value: String = "VIRTUAL_ACCOUNT_ISSUED"
  }
  private object VirtualAccountIssuedSerializer : KSerializer<VirtualAccountIssued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccountIssued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccountIssued = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT_ISSUED") {
        throw SerializationException(it)
      } else {
        return VirtualAccountIssued
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccountIssued) = encoder.encodeString(value.value)
  }
  @Serializable(PaidSerializer::class)
  public data object Paid : PaymentStatus {
    override val value: String = "PAID"
  }
  private object PaidSerializer : KSerializer<Paid> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paid::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paid = decoder.decodeString().let {
      if (it != "PAID") {
        throw SerializationException(it)
      } else {
        return Paid
      }
    }
    override fun serialize(encoder: Encoder, value: Paid) = encoder.encodeString(value.value)
  }
  @Serializable(FailedSerializer::class)
  public data object Failed : PaymentStatus {
    override val value: String = "FAILED"
  }
  private object FailedSerializer : KSerializer<Failed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Failed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Failed = decoder.decodeString().let {
      if (it != "FAILED") {
        throw SerializationException(it)
      } else {
        return Failed
      }
    }
    override fun serialize(encoder: Encoder, value: Failed) = encoder.encodeString(value.value)
  }
  @Serializable(PartialCancelledSerializer::class)
  public data object PartialCancelled : PaymentStatus {
    override val value: String = "PARTIAL_CANCELLED"
  }
  private object PartialCancelledSerializer : KSerializer<PartialCancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartialCancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartialCancelled = decoder.decodeString().let {
      if (it != "PARTIAL_CANCELLED") {
        throw SerializationException(it)
      } else {
        return PartialCancelled
      }
    }
    override fun serialize(encoder: Encoder, value: PartialCancelled) = encoder.encodeString(value.value)
  }
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PaymentStatus {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentStatus
}


private object PaymentStatusSerializer : KSerializer<PaymentStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentStatus::class.java.name, PrimitiveKind.STRING)
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
