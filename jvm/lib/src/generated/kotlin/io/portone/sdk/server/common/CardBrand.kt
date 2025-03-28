package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 카드 브랜드 */
@Serializable(CardBrandSerializer::class)
public sealed interface CardBrand {
  public val value: String
  @Serializable(LocalSerializer::class)
  public data object Local : CardBrand {
    override val value: String = "LOCAL"
  }
  private object LocalSerializer : KSerializer<Local> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Local::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Local = decoder.decodeString().let {
      if (it != "LOCAL") {
        throw SerializationException(it)
      } else {
        return Local
      }
    }
    override fun serialize(encoder: Encoder, value: Local) = encoder.encodeString(value.value)
  }
  @Serializable(MasterSerializer::class)
  public data object Master : CardBrand {
    override val value: String = "MASTER"
  }
  private object MasterSerializer : KSerializer<Master> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Master::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Master = decoder.decodeString().let {
      if (it != "MASTER") {
        throw SerializationException(it)
      } else {
        return Master
      }
    }
    override fun serialize(encoder: Encoder, value: Master) = encoder.encodeString(value.value)
  }
  @Serializable(UnionpaySerializer::class)
  public data object Unionpay : CardBrand {
    override val value: String = "UNIONPAY"
  }
  private object UnionpaySerializer : KSerializer<Unionpay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Unionpay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Unionpay = decoder.decodeString().let {
      if (it != "UNIONPAY") {
        throw SerializationException(it)
      } else {
        return Unionpay
      }
    }
    override fun serialize(encoder: Encoder, value: Unionpay) = encoder.encodeString(value.value)
  }
  @Serializable(VisaSerializer::class)
  public data object Visa : CardBrand {
    override val value: String = "VISA"
  }
  private object VisaSerializer : KSerializer<Visa> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Visa::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Visa = decoder.decodeString().let {
      if (it != "VISA") {
        throw SerializationException(it)
      } else {
        return Visa
      }
    }
    override fun serialize(encoder: Encoder, value: Visa) = encoder.encodeString(value.value)
  }
  @Serializable(JcbSerializer::class)
  public data object Jcb : CardBrand {
    override val value: String = "JCB"
  }
  private object JcbSerializer : KSerializer<Jcb> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Jcb::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Jcb = decoder.decodeString().let {
      if (it != "JCB") {
        throw SerializationException(it)
      } else {
        return Jcb
      }
    }
    override fun serialize(encoder: Encoder, value: Jcb) = encoder.encodeString(value.value)
  }
  @Serializable(AmexSerializer::class)
  public data object Amex : CardBrand {
    override val value: String = "AMEX"
  }
  private object AmexSerializer : KSerializer<Amex> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Amex::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Amex = decoder.decodeString().let {
      if (it != "AMEX") {
        throw SerializationException(it)
      } else {
        return Amex
      }
    }
    override fun serialize(encoder: Encoder, value: Amex) = encoder.encodeString(value.value)
  }
  @Serializable(DinersSerializer::class)
  public data object Diners : CardBrand {
    override val value: String = "DINERS"
  }
  private object DinersSerializer : KSerializer<Diners> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Diners::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Diners = decoder.decodeString().let {
      if (it != "DINERS") {
        throw SerializationException(it)
      } else {
        return Diners
      }
    }
    override fun serialize(encoder: Encoder, value: Diners) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : CardBrand
}


private object CardBrandSerializer : KSerializer<CardBrand> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CardBrand::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): CardBrand {
    val value = decoder.decodeString()
    return when (value) {
      "LOCAL" -> CardBrand.Local
      "MASTER" -> CardBrand.Master
      "UNIONPAY" -> CardBrand.Unionpay
      "VISA" -> CardBrand.Visa
      "JCB" -> CardBrand.Jcb
      "AMEX" -> CardBrand.Amex
      "DINERS" -> CardBrand.Diners
      else -> CardBrand.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: CardBrand) = encoder.encodeString(value.value)
}
