package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 간편 결제 수단 */
@Serializable(EasyPayMethodTypeSerializer::class)
public sealed interface EasyPayMethodType {
  public val value: String
  @Serializable(CardSerializer::class)
  public data object Card : EasyPayMethodType {
    override val value: String = "CARD"
  }
  private object CardSerializer : KSerializer<Card> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Card::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Card = decoder.decodeString().let {
      if (it != "CARD") {
        throw SerializationException(it)
      } else {
        return Card
      }
    }
    override fun serialize(encoder: Encoder, value: Card) = encoder.encodeString(value.value)
  }
  @Serializable(TransferSerializer::class)
  public data object Transfer : EasyPayMethodType {
    override val value: String = "TRANSFER"
  }
  private object TransferSerializer : KSerializer<Transfer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Transfer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Transfer = decoder.decodeString().let {
      if (it != "TRANSFER") {
        throw SerializationException(it)
      } else {
        return Transfer
      }
    }
    override fun serialize(encoder: Encoder, value: Transfer) = encoder.encodeString(value.value)
  }
  @Serializable(ChargeSerializer::class)
  public data object Charge : EasyPayMethodType {
    override val value: String = "CHARGE"
  }
  private object ChargeSerializer : KSerializer<Charge> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Charge::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Charge = decoder.decodeString().let {
      if (it != "CHARGE") {
        throw SerializationException(it)
      } else {
        return Charge
      }
    }
    override fun serialize(encoder: Encoder, value: Charge) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : EasyPayMethodType
}


private object EasyPayMethodTypeSerializer : KSerializer<EasyPayMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EasyPayMethodType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): EasyPayMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> EasyPayMethodType.Card
      "TRANSFER" -> EasyPayMethodType.Transfer
      "CHARGE" -> EasyPayMethodType.Charge
      else -> EasyPayMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: EasyPayMethodType) = encoder.encodeString(value.value)
}
