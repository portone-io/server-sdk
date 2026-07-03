package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 현금영수증 발행여부 */
@Serializable(CashReceiptIssuanceStatusSerializer::class)
public sealed interface CashReceiptIssuanceStatus {
  public val value: String
  /** 발행 완료 */
  @Serializable(IssuedSerializer::class)
  public data object Issued : CashReceiptIssuanceStatus {
    override val value: String = "ISSUED"
  }
  public object IssuedSerializer : KSerializer<Issued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Issued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Issued = decoder.decodeString().let {
      if (it != "ISSUED") {
        throw SerializationException(it)
      } else {
        return Issued
      }
    }
    override fun serialize(encoder: Encoder, value: Issued): Unit = encoder.encodeString(value.value)
  }
  /** 미발행 */
  @Serializable(NotIssuedSerializer::class)
  public data object NotIssued : CashReceiptIssuanceStatus {
    override val value: String = "NOT_ISSUED"
  }
  public object NotIssuedSerializer : KSerializer<NotIssued> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NotIssued::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NotIssued = decoder.decodeString().let {
      if (it != "NOT_ISSUED") {
        throw SerializationException(it)
      } else {
        return NotIssued
      }
    }
    override fun serialize(encoder: Encoder, value: NotIssued): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptIssuanceStatus
}


public object CashReceiptIssuanceStatusSerializer : KSerializer<CashReceiptIssuanceStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptIssuanceStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptIssuanceStatus {
    val value = decoder.decodeString()
    return when (value) {
      "ISSUED" -> CashReceiptIssuanceStatus.Issued
      "NOT_ISSUED" -> CashReceiptIssuanceStatus.NotIssued
      else -> CashReceiptIssuanceStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptIssuanceStatus): Unit = encoder.encodeString(value.value)
}
