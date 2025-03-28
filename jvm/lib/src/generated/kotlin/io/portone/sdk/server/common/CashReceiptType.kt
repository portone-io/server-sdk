package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 발급 유형 */
@Serializable(CashReceiptTypeSerializer::class)
public sealed interface CashReceiptType {
  public val value: String
  /** 소득공제용 */
  @Serializable(PersonalSerializer::class)
  public data object Personal : CashReceiptType {
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
  public data object Corporate : CashReceiptType {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : CashReceiptType
}


private object CashReceiptTypeSerializer : KSerializer<CashReceiptType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CashReceiptType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CashReceiptType {
    val value = decoder.decodeString()
    return when (value) {
      "PERSONAL" -> CashReceiptType.Personal
      "CORPORATE" -> CashReceiptType.Corporate
      else -> CashReceiptType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CashReceiptType) = encoder.encodeString(value.value)
}
