package io.portone.sdk.server.payment.billingkey

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 빌링키 결제 수단 */
@Serializable(BillingKeyPaymentMethodTypeSerializer::class)
public sealed interface BillingKeyPaymentMethodType {
  public val value: String
  /** 카드 */
  @Serializable(CardSerializer::class)
  public data object Card : BillingKeyPaymentMethodType {
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
  /** 모바일 */
  @Serializable(MobileSerializer::class)
  public data object Mobile : BillingKeyPaymentMethodType {
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
  /** 간편 결제 */
  @Serializable(EasyPaySerializer::class)
  public data object EasyPay : BillingKeyPaymentMethodType {
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
  /** 계좌 이체 */
  @Serializable(TransferSerializer::class)
  public data object Transfer : BillingKeyPaymentMethodType {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : BillingKeyPaymentMethodType
}


private object BillingKeyPaymentMethodTypeSerializer : KSerializer<BillingKeyPaymentMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(BillingKeyPaymentMethodType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): BillingKeyPaymentMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> BillingKeyPaymentMethodType.Card
      "MOBILE" -> BillingKeyPaymentMethodType.Mobile
      "EASY_PAY" -> BillingKeyPaymentMethodType.EasyPay
      "TRANSFER" -> BillingKeyPaymentMethodType.Transfer
      else -> BillingKeyPaymentMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: BillingKeyPaymentMethodType) = encoder.encodeString(value.value)
}
