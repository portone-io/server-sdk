package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 가상계좌 환불 상태 */
@Serializable(PaymentMethodVirtualAccountRefundStatusSerializer::class)
public sealed interface PaymentMethodVirtualAccountRefundStatus {
  public val value: String
  /** 처리중 */
  @Serializable(PendingSerializer::class)
  public data object Pending : PaymentMethodVirtualAccountRefundStatus {
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
  /** 부분 환불 실패 */
  @Serializable(PartialRefundFailedSerializer::class)
  public data object PartialRefundFailed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "PARTIAL_REFUND_FAILED"
  }
  private object PartialRefundFailedSerializer : KSerializer<PartialRefundFailed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PartialRefundFailed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): PartialRefundFailed = decoder.decodeString().let {
      if (it != "PARTIAL_REFUND_FAILED") {
        throw SerializationException(it)
      } else {
        return PartialRefundFailed
      }
    }
    override fun serialize(encoder: Encoder, value: PartialRefundFailed) = encoder.encodeString(value.value)
  }
  /** 환불 실패 */
  @Serializable(FailedSerializer::class)
  public data object Failed : PaymentMethodVirtualAccountRefundStatus {
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
  /** 환불 완료 */
  @Serializable(CompletedSerializer::class)
  public data object Completed : PaymentMethodVirtualAccountRefundStatus {
    override val value: String = "COMPLETED"
  }
  private object CompletedSerializer : KSerializer<Completed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Completed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Completed = decoder.decodeString().let {
      if (it != "COMPLETED") {
        throw SerializationException(it)
      } else {
        return Completed
      }
    }
    override fun serialize(encoder: Encoder, value: Completed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodVirtualAccountRefundStatus
}


private object PaymentMethodVirtualAccountRefundStatusSerializer : KSerializer<PaymentMethodVirtualAccountRefundStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodVirtualAccountRefundStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodVirtualAccountRefundStatus {
    val value = decoder.decodeString()
    return when (value) {
      "PENDING" -> PaymentMethodVirtualAccountRefundStatus.Pending
      "PARTIAL_REFUND_FAILED" -> PaymentMethodVirtualAccountRefundStatus.PartialRefundFailed
      "FAILED" -> PaymentMethodVirtualAccountRefundStatus.Failed
      "COMPLETED" -> PaymentMethodVirtualAccountRefundStatus.Completed
      else -> PaymentMethodVirtualAccountRefundStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodVirtualAccountRefundStatus) = encoder.encodeString(value.value)
}
