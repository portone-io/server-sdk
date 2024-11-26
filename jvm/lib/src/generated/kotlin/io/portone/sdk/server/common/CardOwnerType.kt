package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 카드 소유주 유형 */
@Serializable(CardOwnerTypeSerializer::class)
public sealed interface CardOwnerType {
  public val value: String
  /** 개인 */
  @Serializable(PersonalSerializer::class)
  public data object Personal : CardOwnerType {
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
  /** 법인 */
  @Serializable(CorporateSerializer::class)
  public data object Corporate : CardOwnerType {
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
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardOwnerType
}


private object CardOwnerTypeSerializer : KSerializer<CardOwnerType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardOwnerType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CardOwnerType {
    val value = decoder.decodeString()
    return when (value) {
      "PERSONAL" -> CardOwnerType.Personal
      "CORPORATE" -> CardOwnerType.Corporate
      else -> CardOwnerType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CardOwnerType) = encoder.encodeString(value.value)
}
