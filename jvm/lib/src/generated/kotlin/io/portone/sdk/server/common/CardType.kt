package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(CreditSerializer::class)
  public data object Credit : CardType {
    override val value: String = "CREDIT"
  }
  private object CreditSerializer : KSerializer<Credit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Credit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Credit = decoder.decodeString().let {
      if (it != "CREDIT") {
        throw SerializationException(it)
      } else {
        return Credit
      }
    }
    override fun serialize(encoder: Encoder, value: Credit) = encoder.encodeString(value.value)
  }
  /** 체크카드 */
  @Serializable(DebitSerializer::class)
  public data object Debit : CardType {
    override val value: String = "DEBIT"
  }
  private object DebitSerializer : KSerializer<Debit> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Debit::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Debit = decoder.decodeString().let {
      if (it != "DEBIT") {
        throw SerializationException(it)
      } else {
        return Debit
      }
    }
    override fun serialize(encoder: Encoder, value: Debit) = encoder.encodeString(value.value)
  }
  /** 기프트카드 */
  @Serializable(GiftSerializer::class)
  public data object Gift : CardType {
    override val value: String = "GIFT"
  }
  private object GiftSerializer : KSerializer<Gift> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gift::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Gift = decoder.decodeString().let {
      if (it != "GIFT") {
        throw SerializationException(it)
      } else {
        return Gift
      }
    }
    override fun serialize(encoder: Encoder, value: Gift) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : CardType
}


private object CardTypeSerializer : KSerializer<CardType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardType::class.java.name, PrimitiveKind.STRING)
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
