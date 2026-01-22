package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 세금계산서 문서 수정 발행 유형 */
@Serializable(B2bTaxInvoiceDocumentModificationTypeSerializer::class)
public sealed interface B2bTaxInvoiceDocumentModificationType {
  public val value: String
  /** 정상발행 */
  @Serializable(NormalSerializer::class)
  public data object Normal : B2bTaxInvoiceDocumentModificationType {
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
  /** 수정발행 */
  @Serializable(ModificationSerializer::class)
  public data object Modification : B2bTaxInvoiceDocumentModificationType {
    override val value: String = "MODIFICATION"
  }
  public object ModificationSerializer : KSerializer<Modification> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Modification::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Modification = decoder.decodeString().let {
      if (it != "MODIFICATION") {
        throw SerializationException(it)
      } else {
        return Modification
      }
    }
    override fun serialize(encoder: Encoder, value: Modification): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceDocumentModificationType
}


public object B2bTaxInvoiceDocumentModificationTypeSerializer : KSerializer<B2bTaxInvoiceDocumentModificationType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceDocumentModificationType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceDocumentModificationType {
    val value = decoder.decodeString()
    return when (value) {
      "NORMAL" -> B2bTaxInvoiceDocumentModificationType.Normal
      "MODIFICATION" -> B2bTaxInvoiceDocumentModificationType.Modification
      else -> B2bTaxInvoiceDocumentModificationType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceDocumentModificationType): Unit = encoder.encodeString(value.value)
}
