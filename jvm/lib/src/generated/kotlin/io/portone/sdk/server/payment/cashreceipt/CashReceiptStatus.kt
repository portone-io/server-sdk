package io.portone.sdk.server.payment.cashreceipt

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 현금영수증 발급 건 상태 */
@Serializable(CashReceiptStatusSerializer::class)
public sealed interface CashReceiptStatus {
  public val value: String
  @Serializable(IssuedSerializer::class)
  public data object Issued : CashReceiptStatus {
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
  public data object Cancelled : CashReceiptStatus {
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
  @Serializable(FailedSerializer::class)
  public data object Failed : CashReceiptStatus {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptStatus
}


private object CashReceiptStatusSerializer : KSerializer<CashReceiptStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptStatus {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED" -> CashReceiptStatus.Issued
      "CANCELLED" -> CashReceiptStatus.Cancelled
      "FAILED" -> CashReceiptStatus.Failed
      else -> CashReceiptStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptStatus) = encoder.encodeString(value.value)
}
