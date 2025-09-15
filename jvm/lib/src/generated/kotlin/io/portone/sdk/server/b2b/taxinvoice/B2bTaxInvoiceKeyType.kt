package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 세금계산서 식별자 유형 */
@Serializable(B2bTaxInvoiceKeyTypeSerializer::class)
public sealed interface B2bTaxInvoiceKeyType {
  public val value: String
  /** 공급자용 문서 번호 */
  @Serializable(SupplierSerializer::class)
  public data object Supplier : B2bTaxInvoiceKeyType {
    override val value: String = "SUPPLIER"
  }
  private object SupplierSerializer : KSerializer<Supplier> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Supplier::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Supplier = decoder.decodeString().let {
      if (it != "SUPPLIER") {
        throw SerializationException(it)
      } else {
        return Supplier
      }
    }
    override fun serialize(encoder: Encoder, value: Supplier) = encoder.encodeString(value.value)
  }
  /** 공급받는자용 문서 번호 */
  @Serializable(RecipientSerializer::class)
  public data object Recipient : B2bTaxInvoiceKeyType {
    override val value: String = "RECIPIENT"
  }
  private object RecipientSerializer : KSerializer<Recipient> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Recipient::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Recipient = decoder.decodeString().let {
      if (it != "RECIPIENT") {
        throw SerializationException(it)
      } else {
        return Recipient
      }
    }
    override fun serialize(encoder: Encoder, value: Recipient) = encoder.encodeString(value.value)
  }
  /** 세금계산서 아이디 */
  @Serializable(TaxInvoiceIdSerializer::class)
  public data object TaxInvoiceId : B2bTaxInvoiceKeyType {
    override val value: String = "TAX_INVOICE_ID"
  }
  private object TaxInvoiceIdSerializer : KSerializer<TaxInvoiceId> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(TaxInvoiceId::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): TaxInvoiceId = decoder.decodeString().let {
      if (it != "TAX_INVOICE_ID") {
        throw SerializationException(it)
      } else {
        return TaxInvoiceId
      }
    }
    override fun serialize(encoder: Encoder, value: TaxInvoiceId) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceKeyType
}


private object B2bTaxInvoiceKeyTypeSerializer : KSerializer<B2bTaxInvoiceKeyType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceKeyType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceKeyType {
    val value = decoder.decodeString()
    return when (value) {
      "SUPPLIER" -> B2bTaxInvoiceKeyType.Supplier
      "RECIPIENT" -> B2bTaxInvoiceKeyType.Recipient
      "TAX_INVOICE_ID" -> B2bTaxInvoiceKeyType.TaxInvoiceId
      else -> B2bTaxInvoiceKeyType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceKeyType) = encoder.encodeString(value.value)
}
