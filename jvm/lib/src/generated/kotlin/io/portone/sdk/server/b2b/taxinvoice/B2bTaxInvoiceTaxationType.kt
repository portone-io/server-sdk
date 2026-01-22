package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 과세 유형 */
@Serializable(B2bTaxInvoiceTaxationTypeSerializer::class)
public sealed interface B2bTaxInvoiceTaxationType {
  public val value: String
  /** 과세 */
  @Serializable(TaxableSerializer::class)
  public data object Taxable : B2bTaxInvoiceTaxationType {
    override val value: String = "TAXABLE"
  }
  public object TaxableSerializer : KSerializer<Taxable> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Taxable::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Taxable = decoder.decodeString().let {
      if (it != "TAXABLE") {
        throw SerializationException(it)
      } else {
        return Taxable
      }
    }
    override fun serialize(encoder: Encoder, value: Taxable): Unit = encoder.encodeString(value.value)
  }
  /** 영세 */
  @Serializable(ZeroRatedSerializer::class)
  public data object ZeroRated : B2bTaxInvoiceTaxationType {
    override val value: String = "ZERO_RATED"
  }
  public object ZeroRatedSerializer : KSerializer<ZeroRated> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(ZeroRated::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): ZeroRated = decoder.decodeString().let {
      if (it != "ZERO_RATED") {
        throw SerializationException(it)
      } else {
        return ZeroRated
      }
    }
    override fun serialize(encoder: Encoder, value: ZeroRated): Unit = encoder.encodeString(value.value)
  }
  /** 면세 */
  @Serializable(FreeSerializer::class)
  public data object Free : B2bTaxInvoiceTaxationType {
    override val value: String = "FREE"
  }
  public object FreeSerializer : KSerializer<Free> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Free::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Free = decoder.decodeString().let {
      if (it != "FREE") {
        throw SerializationException(it)
      } else {
        return Free
      }
    }
    override fun serialize(encoder: Encoder, value: Free): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceTaxationType
}


public object B2bTaxInvoiceTaxationTypeSerializer : KSerializer<B2bTaxInvoiceTaxationType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceTaxationType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceTaxationType {
    val value = decoder.decodeString()
    return when (value) {
      "TAXABLE" -> B2bTaxInvoiceTaxationType.Taxable
      "ZERO_RATED" -> B2bTaxInvoiceTaxationType.ZeroRated
      "FREE" -> B2bTaxInvoiceTaxationType.Free
      else -> B2bTaxInvoiceTaxationType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceTaxationType): Unit = encoder.encodeString(value.value)
}
