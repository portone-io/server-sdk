package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제건 내 현금영수증 상태 */
@Serializable(PaymentCashReceiptStatusSerializer::class)
public sealed interface PaymentCashReceiptStatus {
  public val value: String
  @Serializable(IssuedSerializer::class)
  public data object Issued : PaymentCashReceiptStatus {
    override val value: String = "ISSUED"
  }
  private object IssuedSerializer : KSerializer<Issued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Issued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Issued = decoder.decodeString().let {
      if (it != "ISSUED") {
        throw SerializationException(it)
      } else {
        return Issued
      }
    }
    override fun serialize(encoder: Encoder, value: Issued) = encoder.encodeString(value.value)
  }
  @Serializable(CancelledSerializer::class)
  public data object Cancelled : PaymentCashReceiptStatus {
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
  public data class Unrecognized internal constructor(override val value: String) : PaymentCashReceiptStatus
}


private object PaymentCashReceiptStatusSerializer : KSerializer<PaymentCashReceiptStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentCashReceiptStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentCashReceiptStatus {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED" -> PaymentCashReceiptStatus.Issued
      "CANCELLED" -> PaymentCashReceiptStatus.Cancelled
      else -> PaymentCashReceiptStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentCashReceiptStatus) = encoder.encodeString(value.value)
}
