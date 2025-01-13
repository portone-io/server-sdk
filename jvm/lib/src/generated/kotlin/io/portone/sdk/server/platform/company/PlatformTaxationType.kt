package io.portone.sdk.server.platform.company

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 과세 유형 */
@Serializable(PlatformTaxationTypeSerializer::class)
public sealed interface PlatformTaxationType {
  public val value: String
  /** 일반 과세 */
  @Serializable(NormalSerializer::class)
  public data object Normal : PlatformTaxationType {
    override val value: String = "NORMAL"
  }
  private object NormalSerializer : KSerializer<Normal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Normal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Normal = decoder.decodeString().let {
      if (it != "NORMAL") {
        throw SerializationException(it)
      } else {
        return Normal
      }
    }
    override fun serialize(encoder: Encoder, value: Normal) = encoder.encodeString(value.value)
  }
  /** 간이과세(세금계산서 발행) */
  @Serializable(SimpleTaxInvoiceIssuerSerializer::class)
  public data object SimpleTaxInvoiceIssuer : PlatformTaxationType {
    override val value: String = "SIMPLE_TAX_INVOICE_ISSUER"
  }
  private object SimpleTaxInvoiceIssuerSerializer : KSerializer<SimpleTaxInvoiceIssuer> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SimpleTaxInvoiceIssuer::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SimpleTaxInvoiceIssuer = decoder.decodeString().let {
      if (it != "SIMPLE_TAX_INVOICE_ISSUER") {
        throw SerializationException(it)
      } else {
        return SimpleTaxInvoiceIssuer
      }
    }
    override fun serialize(encoder: Encoder, value: SimpleTaxInvoiceIssuer) = encoder.encodeString(value.value)
  }
  /** 간이과세(세금계산서 미발행) */
  @Serializable(SimpleSerializer::class)
  public data object Simple : PlatformTaxationType {
    override val value: String = "SIMPLE"
  }
  private object SimpleSerializer : KSerializer<Simple> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Simple::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Simple = decoder.decodeString().let {
      if (it != "SIMPLE") {
        throw SerializationException(it)
      } else {
        return Simple
      }
    }
    override fun serialize(encoder: Encoder, value: Simple) = encoder.encodeString(value.value)
  }
  /** 면세 */
  @Serializable(TaxFreeSerializer::class)
  public data object TaxFree : PlatformTaxationType {
    override val value: String = "TAX_FREE"
  }
  private object TaxFreeSerializer : KSerializer<TaxFree> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TaxFree::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TaxFree = decoder.decodeString().let {
      if (it != "TAX_FREE") {
        throw SerializationException(it)
      } else {
        return TaxFree
      }
    }
    override fun serialize(encoder: Encoder, value: TaxFree) = encoder.encodeString(value.value)
  }
  /** 고유 번호 부여 사업자 (비영리, 국가 등 납세 의무가 없는) */
  @Serializable(AssignedIdNumberSerializer::class)
  public data object AssignedIdNumber : PlatformTaxationType {
    override val value: String = "ASSIGNED_ID_NUMBER"
  }
  private object AssignedIdNumberSerializer : KSerializer<AssignedIdNumber> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(AssignedIdNumber::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): AssignedIdNumber = decoder.decodeString().let {
      if (it != "ASSIGNED_ID_NUMBER") {
        throw SerializationException(it)
      } else {
        return AssignedIdNumber
      }
    }
    override fun serialize(encoder: Encoder, value: AssignedIdNumber) = encoder.encodeString(value.value)
  }
  /** 과세 특례자 */
  @Serializable(SpecialSerializer::class)
  public data object Special : PlatformTaxationType {
    override val value: String = "SPECIAL"
  }
  private object SpecialSerializer : KSerializer<Special> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Special::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Special = decoder.decodeString().let {
      if (it != "SPECIAL") {
        throw SerializationException(it)
      } else {
        return Special
      }
    }
    override fun serialize(encoder: Encoder, value: Special) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTaxationType
}


private object PlatformTaxationTypeSerializer : KSerializer<PlatformTaxationType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTaxationType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTaxationType {
    val value = decoder.decodeString()
    return when (value) {
      "NORMAL" -> PlatformTaxationType.Normal
      "SIMPLE_TAX_INVOICE_ISSUER" -> PlatformTaxationType.SimpleTaxInvoiceIssuer
      "SIMPLE" -> PlatformTaxationType.Simple
      "TAX_FREE" -> PlatformTaxationType.TaxFree
      "ASSIGNED_ID_NUMBER" -> PlatformTaxationType.AssignedIdNumber
      "SPECIAL" -> PlatformTaxationType.Special
      else -> PlatformTaxationType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTaxationType) = encoder.encodeString(value.value)
}
