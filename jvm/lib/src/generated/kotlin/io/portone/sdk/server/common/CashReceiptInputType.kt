package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 입력 시 발급 유형 */
@Serializable(CashReceiptInputTypeSerializer::class)
public sealed interface CashReceiptInputType {
  public val value: String
  /** 소득공제용 */
  @Serializable(PersonalSerializer::class)
  public data object Personal : CashReceiptInputType {
    override val value: String = "PERSONAL"
  }
  private object PersonalSerializer : KSerializer<Personal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Personal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Personal = decoder.decodeString().let {
      if (it != "PERSONAL") {
        throw SerializationException(it)
      } else {
        return Personal
      }
    }
    override fun serialize(encoder: Encoder, value: Personal) = encoder.encodeString(value.value)
  }
  /** 지출증빙용 */
  @Serializable(CorporateSerializer::class)
  public data object Corporate : CashReceiptInputType {
    override val value: String = "CORPORATE"
  }
  private object CorporateSerializer : KSerializer<Corporate> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Corporate::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Corporate = decoder.decodeString().let {
      if (it != "CORPORATE") {
        throw SerializationException(it)
      } else {
        return Corporate
      }
    }
    override fun serialize(encoder: Encoder, value: Corporate) = encoder.encodeString(value.value)
  }
  /**
   * 미발행
   *
   * PG사 설정에 따라 PG사가 자동으로 자진발급 처리할 수 있습니다.
   */
  @Serializable(NoReceiptSerializer::class)
  public data object NoReceipt : CashReceiptInputType {
    override val value: String = "NO_RECEIPT"
  }
  private object NoReceiptSerializer : KSerializer<NoReceipt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(NoReceipt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): NoReceipt = decoder.decodeString().let {
      if (it != "NO_RECEIPT") {
        throw SerializationException(it)
      } else {
        return NoReceipt
      }
    }
    override fun serialize(encoder: Encoder, value: NoReceipt) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptInputType
}


private object CashReceiptInputTypeSerializer : KSerializer<CashReceiptInputType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptInputType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptInputType {
    val value = decoder.decodeString()
    return when (value) {
      "PERSONAL" -> CashReceiptInputType.Personal
      "CORPORATE" -> CashReceiptInputType.Corporate
      "NO_RECEIPT" -> CashReceiptInputType.NoReceipt
      else -> CashReceiptInputType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptInputType) = encoder.encodeString(value.value)
}
