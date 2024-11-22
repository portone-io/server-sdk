package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 카드 유형 */
@Serializable(CardTypeSerializer::class)
public sealed interface CardType {
  public val value: String
  /** 신용카드 */
  public data object Credit : CardType {
    override val value: String = "CREDIT"
  }
  /** 체크카드 */
  public data object Debit : CardType {
    override val value: String = "DEBIT"
  }
  /** 기프트카드 */
  public data object Gift : CardType {
    override val value: String = "GIFT"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CardType
}


private object CardTypeSerializer : KSerializer<CardType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CardType {
    val value = decoder.decodeString()
    return when (value) {
      "CREDIT" -> CardType.Credit
      "DEBIT" -> CardType.Debit
      "GIFT" -> CardType.Gift
      else -> CardType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CardType) = encoder.encodeString(value.value)
}
