package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PaymentMethodTypeSerializer::class)
public sealed interface PaymentMethodType {
  public val value: String
  public data object Card : PaymentMethodType {
    override val value: String = "CARD"
  }
  public data object Transfer : PaymentMethodType {
    override val value: String = "TRANSFER"
  }
  public data object VirtualAccount : PaymentMethodType {
    override val value: String = "VIRTUAL_ACCOUNT"
  }
  public data object GiftCertificate : PaymentMethodType {
    override val value: String = "GIFT_CERTIFICATE"
  }
  public data object Mobile : PaymentMethodType {
    override val value: String = "MOBILE"
  }
  public data object EasyPay : PaymentMethodType {
    override val value: String = "EASY_PAY"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodType
}


private object PaymentMethodTypeSerializer : KSerializer<PaymentMethodType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodType {
    val value = decoder.decodeString()
    return when (value) {
      "CARD" -> PaymentMethodType.Card
      "TRANSFER" -> PaymentMethodType.Transfer
      "VIRTUAL_ACCOUNT" -> PaymentMethodType.VirtualAccount
      "GIFT_CERTIFICATE" -> PaymentMethodType.GiftCertificate
      "MOBILE" -> PaymentMethodType.Mobile
      "EASY_PAY" -> PaymentMethodType.EasyPay
      else -> PaymentMethodType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodType) = encoder.encodeString(value.value)
}
