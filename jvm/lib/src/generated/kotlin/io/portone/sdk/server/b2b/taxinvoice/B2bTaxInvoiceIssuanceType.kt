package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 발행 유형 */
@Serializable(B2bTaxInvoiceIssuanceTypeSerializer::class)
public sealed interface B2bTaxInvoiceIssuanceType {
  public val value: String
  /** 정발행 */
  @Serializable(NormalSerializer::class)
  public data object Normal : B2bTaxInvoiceIssuanceType {
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
  /** 역발행 */
  @Serializable(ReverseSerializer::class)
  public data object Reverse : B2bTaxInvoiceIssuanceType {
    override val value: String = "REVERSE"
  }
  public object ReverseSerializer : KSerializer<Reverse> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Reverse::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Reverse = decoder.decodeString().let {
      if (it != "REVERSE") {
        throw SerializationException(it)
      } else {
        return Reverse
      }
    }
    override fun serialize(encoder: Encoder, value: Reverse): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bTaxInvoiceIssuanceType
}


public object B2bTaxInvoiceIssuanceTypeSerializer : KSerializer<B2bTaxInvoiceIssuanceType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bTaxInvoiceIssuanceType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bTaxInvoiceIssuanceType {
    val value = decoder.decodeString()
    return when (value) {
      "NORMAL" -> B2bTaxInvoiceIssuanceType.Normal
      "REVERSE" -> B2bTaxInvoiceIssuanceType.Reverse
      else -> B2bTaxInvoiceIssuanceType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bTaxInvoiceIssuanceType): Unit = encoder.encodeString(value.value)
}
