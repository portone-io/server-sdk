package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 상품권 종류 */
@Serializable(PaymentMethodGiftCertificateTypeSerializer::class)
public sealed interface PaymentMethodGiftCertificateType {
  public val value: String
  @Serializable(BooknlifeSerializer::class)
  public data object Booknlife : PaymentMethodGiftCertificateType {
    override val value: String = "BOOKNLIFE"
  }
  private object BooknlifeSerializer : KSerializer<Booknlife> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Booknlife::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Booknlife = decoder.decodeString().let {
      if (it != "BOOKNLIFE") {
        throw SerializationException(it)
      } else {
        return Booknlife
      }
    }
    override fun serialize(encoder: Encoder, value: Booknlife) = encoder.encodeString(value.value)
  }
  @Serializable(SmartMunsangSerializer::class)
  public data object SmartMunsang : PaymentMethodGiftCertificateType {
    override val value: String = "SMART_MUNSANG"
  }
  private object SmartMunsangSerializer : KSerializer<SmartMunsang> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SmartMunsang::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SmartMunsang = decoder.decodeString().let {
      if (it != "SMART_MUNSANG") {
        throw SerializationException(it)
      } else {
        return SmartMunsang
      }
    }
    override fun serialize(encoder: Encoder, value: SmartMunsang) = encoder.encodeString(value.value)
  }
  @Serializable(CulturelandSerializer::class)
  public data object Cultureland : PaymentMethodGiftCertificateType {
    override val value: String = "CULTURELAND"
  }
  private object CulturelandSerializer : KSerializer<Cultureland> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Cultureland::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Cultureland = decoder.decodeString().let {
      if (it != "CULTURELAND") {
        throw SerializationException(it)
      } else {
        return Cultureland
      }
    }
    override fun serialize(encoder: Encoder, value: Cultureland) = encoder.encodeString(value.value)
  }
  @Serializable(HappymoneySerializer::class)
  public data object Happymoney : PaymentMethodGiftCertificateType {
    override val value: String = "HAPPYMONEY"
  }
  private object HappymoneySerializer : KSerializer<Happymoney> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Happymoney::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Happymoney = decoder.decodeString().let {
      if (it != "HAPPYMONEY") {
        throw SerializationException(it)
      } else {
        return Happymoney
      }
    }
    override fun serialize(encoder: Encoder, value: Happymoney) = encoder.encodeString(value.value)
  }
  @Serializable(CulturegiftSerializer::class)
  public data object Culturegift : PaymentMethodGiftCertificateType {
    override val value: String = "CULTUREGIFT"
  }
  private object CulturegiftSerializer : KSerializer<Culturegift> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Culturegift::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Culturegift = decoder.decodeString().let {
      if (it != "CULTUREGIFT") {
        throw SerializationException(it)
      } else {
        return Culturegift
      }
    }
    override fun serialize(encoder: Encoder, value: Culturegift) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodGiftCertificateType
}


private object PaymentMethodGiftCertificateTypeSerializer : KSerializer<PaymentMethodGiftCertificateType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodGiftCertificateType::class.java.name, PrimitiveKind.STRING)
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
