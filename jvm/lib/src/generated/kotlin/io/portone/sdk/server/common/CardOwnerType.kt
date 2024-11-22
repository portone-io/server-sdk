package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Personal : CardOwnerType {
    override val value: String = "PERSONAL"
  }
  /** 법인 */
  public data object Corporate : CardOwnerType {
    override val value: String = "CORPORATE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardOwnerType
}


private object CardOwnerTypeSerializer : KSerializer<CardOwnerType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardOwnerType::class.java.canonicalName, PrimitiveKind.STRING)
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
