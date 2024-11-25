package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 상품권 종류 */
@Serializable(PaymentMethodGiftCertificateTypeSerializer::class)
public sealed interface PaymentMethodGiftCertificateType {
  public val value: String
  public data object Booknlife : PaymentMethodGiftCertificateType {
    override val value: String = "BOOKNLIFE"
  }
  public data object SmartMunsang : PaymentMethodGiftCertificateType {
    override val value: String = "SMART_MUNSANG"
  }
  public data object Cultureland : PaymentMethodGiftCertificateType {
    override val value: String = "CULTURELAND"
  }
  public data object Happymoney : PaymentMethodGiftCertificateType {
    override val value: String = "HAPPYMONEY"
  }
  public data object Culturegift : PaymentMethodGiftCertificateType {
    override val value: String = "CULTUREGIFT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodGiftCertificateType
}


private object PaymentMethodGiftCertificateTypeSerializer : KSerializer<PaymentMethodGiftCertificateType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodGiftCertificateType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodGiftCertificateType {
    val value = decoder.decodeString()
    return when (value) {
      "BOOKNLIFE" -> PaymentMethodGiftCertificateType.Booknlife
      "SMART_MUNSANG" -> PaymentMethodGiftCertificateType.SmartMunsang
      "CULTURELAND" -> PaymentMethodGiftCertificateType.Cultureland
      "HAPPYMONEY" -> PaymentMethodGiftCertificateType.Happymoney
      "CULTUREGIFT" -> PaymentMethodGiftCertificateType.Culturegift
      else -> PaymentMethodGiftCertificateType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodGiftCertificateType) = encoder.encodeString(value.value)
}
