package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 파트너 과세 유형 */
@Serializable(PlatformPartnerTaxationTypeSerializer::class)
public sealed interface PlatformPartnerTaxationType {
  public val value: String
  /** 일반 과세 */
  @Serializable(NormalSerializer::class)
  public data object Normal : PlatformPartnerTaxationType {
    override val value: String = "NORMAL"
  }
  public object NormalSerializer : KSerializer<Normal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Normal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Normal = decoder.decodeString().let {
      if (it != "NORMAL") {
        throw SerializationException(it)
      } else {
        return Normal
      }
    }
    override fun serialize(encoder: Encoder, value: Normal): Unit = encoder.encodeString(value.value)
  }
  /** 간이과세(세금계산서 발행) */
  @Serializable(SimpleTaxInvoiceIssuerSerializer::class)
  public data object SimpleTaxInvoiceIssuer : PlatformPartnerTaxationType {
    override val value: String = "SIMPLE_TAX_INVOICE_ISSUER"
  }
  public object SimpleTaxInvoiceIssuerSerializer : KSerializer<SimpleTaxInvoiceIssuer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SimpleTaxInvoiceIssuer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SimpleTaxInvoiceIssuer = decoder.decodeString().let {
      if (it != "SIMPLE_TAX_INVOICE_ISSUER") {
        throw SerializationException(it)
      } else {
        return SimpleTaxInvoiceIssuer
      }
    }
    override fun serialize(encoder: Encoder, value: SimpleTaxInvoiceIssuer): Unit = encoder.encodeString(value.value)
  }
  /** 간이과세(세금계산서 미발행) */
  @Serializable(SimpleSerializer::class)
  public data object Simple : PlatformPartnerTaxationType {
    override val value: String = "SIMPLE"
  }
  public object SimpleSerializer : KSerializer<Simple> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Simple::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Simple = decoder.decodeString().let {
      if (it != "SIMPLE") {
        throw SerializationException(it)
      } else {
        return Simple
      }
    }
    override fun serialize(encoder: Encoder, value: Simple): Unit = encoder.encodeString(value.value)
  }
  /** 면세 */
  @Serializable(TaxFreeSerializer::class)
  public data object TaxFree : PlatformPartnerTaxationType {
    override val value: String = "TAX_FREE"
  }
  public object TaxFreeSerializer : KSerializer<TaxFree> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TaxFree::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TaxFree = decoder.decodeString().let {
      if (it != "TAX_FREE") {
        throw SerializationException(it)
      } else {
        return TaxFree
      }
    }
    override fun serialize(encoder: Encoder, value: TaxFree): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerTaxationType
}


public object PlatformPartnerTaxationTypeSerializer : KSerializer<PlatformPartnerTaxationType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerTaxationType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerTaxationType {
    val value = decoder.decodeString()
    return when (value) {
      "NORMAL" -> PlatformPartnerTaxationType.Normal
      "SIMPLE_TAX_INVOICE_ISSUER" -> PlatformPartnerTaxationType.SimpleTaxInvoiceIssuer
      "SIMPLE" -> PlatformPartnerTaxationType.Simple
      "TAX_FREE" -> PlatformPartnerTaxationType.TaxFree
      else -> PlatformPartnerTaxationType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerTaxationType): Unit = encoder.encodeString(value.value)
}
