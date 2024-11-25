package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Normal : PlatformPartnerTaxationType {
    override val value: String = "NORMAL"
  }
  /** 간이과세(세금계산서 발행) */
  public data object SimpleTaxInvoiceIssuer : PlatformPartnerTaxationType {
    override val value: String = "SIMPLE_TAX_INVOICE_ISSUER"
  }
  /** 간이과세(세금계산서 미발행) */
  public data object Simple : PlatformPartnerTaxationType {
    override val value: String = "SIMPLE"
  }
  /** 면세 */
  public data object TaxFree : PlatformPartnerTaxationType {
    override val value: String = "TAX_FREE"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerTaxationType
}


private object PlatformPartnerTaxationTypeSerializer : KSerializer<PlatformPartnerTaxationType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerTaxationType::class.java.canonicalName, PrimitiveKind.STRING)
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
  override fun serialize(encoder: Encoder, value: PlatformPartnerTaxationType) = encoder.encodeString(value.value)
}
