package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PaymentMethodTypeSerializer::class)
public sealed interface PaymentMethodType {
  public val value: String
  @Serializable(CardSerializer::class)
  public data object Card : PaymentMethodType {
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
  public data object Transfer : PaymentMethodType {
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
  @Serializable(VirtualAccountSerializer::class)
  public data object VirtualAccount : PaymentMethodType {
    override val value: String = "VIRTUAL_ACCOUNT"
  }
  private object VirtualAccountSerializer : KSerializer<VirtualAccount> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(VirtualAccount::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): VirtualAccount = decoder.decodeString().let {
      if (it != "VIRTUAL_ACCOUNT") {
        throw SerializationException(it)
      } else {
        return VirtualAccount
      }
    }
    override fun serialize(encoder: Encoder, value: VirtualAccount) = encoder.encodeString(value.value)
  }
  @Serializable(GiftCertificateSerializer::class)
  public data object GiftCertificate : PaymentMethodType {
    override val value: String = "GIFT_CERTIFICATE"
  }
  private object GiftCertificateSerializer : KSerializer<GiftCertificate> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(GiftCertificate::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): GiftCertificate = decoder.decodeString().let {
      if (it != "GIFT_CERTIFICATE") {
        throw SerializationException(it)
      } else {
        return GiftCertificate
      }
    }
    override fun serialize(encoder: Encoder, value: GiftCertificate) = encoder.encodeString(value.value)
  }
  @Serializable(MobileSerializer::class)
  public data object Mobile : PaymentMethodType {
    override val value: String = "MOBILE"
  }
  private object MobileSerializer : KSerializer<Mobile> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mobile::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mobile = decoder.decodeString().let {
      if (it != "MOBILE") {
        throw SerializationException(it)
      } else {
        return Mobile
      }
    }
    override fun serialize(encoder: Encoder, value: Mobile) = encoder.encodeString(value.value)
  }
  @Serializable(EasyPaySerializer::class)
  public data object EasyPay : PaymentMethodType {
    override val value: String = "EASY_PAY"
  }
  private object EasyPaySerializer : KSerializer<EasyPay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(EasyPay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): EasyPay = decoder.decodeString().let {
      if (it != "EASY_PAY") {
        throw SerializationException(it)
      } else {
        return EasyPay
      }
    }
    override fun serialize(encoder: Encoder, value: EasyPay) = encoder.encodeString(value.value)
  }
  @Serializable(ConvenienceStoreSerializer::class)
  public data object ConvenienceStore : PaymentMethodType {
    override val value: String = "CONVENIENCE_STORE"
  }
  private object ConvenienceStoreSerializer : KSerializer<ConvenienceStore> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ConvenienceStore::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ConvenienceStore = decoder.decodeString().let {
      if (it != "CONVENIENCE_STORE") {
        throw SerializationException(it)
      } else {
        return ConvenienceStore
      }
    }
    override fun serialize(encoder: Encoder, value: ConvenienceStore) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodType
}


private object PaymentMethodTypeSerializer : KSerializer<PaymentMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> PaymentMethodType.Card
      "TRANSFER" -> PaymentMethodType.Transfer
      "VIRTUAL_ACCOUNT" -> PaymentMethodType.VirtualAccount
      "GIFT_CERTIFICATE" -> PaymentMethodType.GiftCertificate
      "MOBILE" -> PaymentMethodType.Mobile
      "EASY_PAY" -> PaymentMethodType.EasyPay
      "CONVENIENCE_STORE" -> PaymentMethodType.ConvenienceStore
      else -> PaymentMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodType) = encoder.encodeString(value.value)
}
