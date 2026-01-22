package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 영수/청구 */
@Serializable(B2bTaxInvoicePurposeTypeSerializer::class)
public sealed interface B2bTaxInvoicePurposeType {
  public val value: String
  /** 영수 */
  @Serializable(ReceiptSerializer::class)
  public data object Receipt : B2bTaxInvoicePurposeType {
    override val value: String = "RECEIPT"
  }
  public object ReceiptSerializer : KSerializer<Receipt> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Receipt::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Receipt = decoder.decodeString().let {
      if (it != "RECEIPT") {
        throw SerializationException(it)
      } else {
        return Receipt
      }
    }
    override fun serialize(encoder: Encoder, value: Receipt): Unit = encoder.encodeString(value.value)
  }
  /** 청구 */
  @Serializable(InvoiceSerializer::class)
  public data object Invoice : B2bTaxInvoicePurposeType {
    override val value: String = "INVOICE"
  }
  public object InvoiceSerializer : KSerializer<Invoice> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Invoice::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Invoice = decoder.decodeString().let {
      if (it != "INVOICE") {
        throw SerializationException(it)
      } else {
        return Invoice
      }
    }
    override fun serialize(encoder: Encoder, value: Invoice): Unit = encoder.encodeString(value.value)
  }
  /** 없음 */
  @Serializable(NoneSerializer::class)
  public data object None : B2bTaxInvoicePurposeType {
    override val value: String = "NONE"
  }
  public object NoneSerializer : KSerializer<None> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(None::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): None = decoder.decodeString().let {
      if (it != "NONE") {
        throw SerializationException(it)
      } else {
        return None
      }
    }
    override fun serialize(encoder: Encoder, value: None): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoicePurposeType
}


public object B2bTaxInvoicePurposeTypeSerializer : KSerializer<B2bTaxInvoicePurposeType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoicePurposeType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoicePurposeType {
    val value = decoder.decodeString()
    return when (value) {
      "RECEIPT" -> B2bTaxInvoicePurposeType.Receipt
      "INVOICE" -> B2bTaxInvoicePurposeType.Invoice
      "NONE" -> B2bTaxInvoicePurposeType.None
      else -> B2bTaxInvoicePurposeType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoicePurposeType): Unit = encoder.encodeString(value.value)
}
