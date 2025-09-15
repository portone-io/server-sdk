package io.portone.sdk.server.b2b.taxinvoice

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 그룹 생성 방식 */
@Serializable(B2bBulkTaxInvoiceSourceTypeSerializer::class)
public sealed interface B2bBulkTaxInvoiceSourceType {
  public val value: String
  /** 엑셀 업로드 */
  @Serializable(SheetSerializer::class)
  public data object Sheet : B2bBulkTaxInvoiceSourceType {
    override val value: String = "SHEET"
  }
  private object SheetSerializer : KSerializer<Sheet> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sheet::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sheet = decoder.decodeString().let {
      if (it != "SHEET") {
        throw SerializationException(it)
      } else {
        return Sheet
      }
    }
    override fun serialize(encoder: Encoder, value: Sheet) = encoder.encodeString(value.value)
  }
  /** 지급 데이터 기반 생성 */
  @Serializable(PlatformSerializer::class)
  public data object Platform : B2bBulkTaxInvoiceSourceType {
    override val value: String = "PLATFORM"
  }
  private object PlatformSerializer : KSerializer<Platform> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Platform::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Platform = decoder.decodeString().let {
      if (it != "PLATFORM") {
        throw SerializationException(it)
      } else {
        return Platform
      }
    }
    override fun serialize(encoder: Encoder, value: Platform) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : B2bBulkTaxInvoiceSourceType
}


private object B2bBulkTaxInvoiceSourceTypeSerializer : KSerializer<B2bBulkTaxInvoiceSourceType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(B2bBulkTaxInvoiceSourceType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): B2bBulkTaxInvoiceSourceType {
    val value = decoder.decodeString()
    return when (value) {
      "SHEET" -> B2bBulkTaxInvoiceSourceType.Sheet
      "PLATFORM" -> B2bBulkTaxInvoiceSourceType.Platform
      else -> B2bBulkTaxInvoiceSourceType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: B2bBulkTaxInvoiceSourceType) = encoder.encodeString(value.value)
}
