package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 웹훅 발송 시 결제 건 상태 */
@Serializable(PaymentWebhookPaymentStatusSerializer::class)
public sealed interface PaymentWebhookPaymentStatus {
  public val value: String
  @Serializable(ReadySerializer::class)
  public data object Ready : PaymentWebhookPaymentStatus {
    override val value: String = "READY"
  }
  public object ReadySerializer : KSerializer<Ready> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Ready::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Ready = decoder.decodeString().let {
      if (it != "READY") {
        throw SerializationException(it)
      } else {
        return Ready
      }
    }
    override fun serialize(encoder: Encoder, value: Ready): Unit = encoder.encodeString(value.value)
  }
  @Serializable(VirtualAccountIssuedSerializer::class)
  public data object VirtualAccountIssued : PaymentWebhookPaymentStatus {
    override val value: String = "VIRTUAL_ACCOUNT_ISSUED"
  }
  public object VirtualAccountIssuedSerializer : KSerializer<VirtualAccountIssued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccountIssued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccountIssued = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT_ISSUED") {
        throw SerializationException(it)
      } else {
        return VirtualAccountIssued
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccountIssued): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PaidSerializer::class)
  public data object Paid : PaymentWebhookPaymentStatus {
    override val value: String = "PAID"
  }
  public object PaidSerializer : KSerializer<Paid> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Paid::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Paid = decoder.decodeString().let {
      if (it != "PAID") {
        throw SerializationException(it)
      } else {
        return Paid
      }
    }
    override fun serialize(encoder: Encoder, value: Paid): Unit = encoder.encodeString(value.value)
  }
  @Serializable(FailedSerializer::class)
  public data object Failed : PaymentWebhookPaymentStatus {
    override val value: String = "FAILED"
  }
  public object FailedSerializer : KSerializer<Failed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Failed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Failed = decoder.decodeString().let {
      if (it != "FAILED") {
        throw SerializationException(it)
      } else {
        return Failed
      }
    }
    override fun serialize(encoder: Encoder, value: Failed): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PartialCancelledSerializer::class)
  public data object PartialCancelled : PaymentWebhookPaymentStatus {
    override val value: String = "PARTIAL_CANCELLED"
  }
  public object PartialCancelledSerializer : KSerializer<PartialCancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartialCancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartialCancelled = decoder.decodeString().let {
      if (it != "PARTIAL_CANCELLED") {
        throw SerializationException(it)
      } else {
        return PartialCancelled
      }
    }
    override fun serialize(encoder: Encoder, value: PartialCancelled): Unit = encoder.encodeString(value.value)
  }
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PaymentWebhookPaymentStatus {
    override val value: String = "CANCELLED"
  }
  public object CancelledSerializer : KSerializer<Cancelled> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cancelled::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cancelled = decoder.decodeString().let {
      if (it != "CANCELLED") {
        throw SerializationException(it)
      } else {
        return Cancelled
      }
    }
    override fun serialize(encoder: Encoder, value: Cancelled): Unit = encoder.encodeString(value.value)
  }
  @Serializable(PayPendingSerializer::class)
  public data object PayPending : PaymentWebhookPaymentStatus {
    override val value: String = "PAY_PENDING"
  }
  public object PayPendingSerializer : KSerializer<PayPending> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PayPending::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PayPending = decoder.decodeString().let {
      if (it != "PAY_PENDING") {
        throw SerializationException(it)
      } else {
        return PayPending
      }
    }
    override fun serialize(encoder: Encoder, value: PayPending): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentWebhookPaymentStatus
}


public object PaymentWebhookPaymentStatusSerializer : KSerializer<PaymentWebhookPaymentStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentWebhookPaymentStatus::class.java.name, PrimitiveKind.STRING)
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
  override fun serialize(encoder: Encoder, value: PaymentWebhookPaymentStatus): Unit = encoder.encodeString(value.value)
}
