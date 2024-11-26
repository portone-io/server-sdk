package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 금액 타입 */
@Serializable(PlatformCancellableAmountTypeSerializer::class)
public sealed interface PlatformCancellableAmountType {
  public val value: String
  /**
   * 공급대가
   *
   * 공급가액과 부가세를 더한 금액입니다.
   */
  @Serializable(SupplyWithVatSerializer::class)
  public data object SupplyWithVat : PlatformCancellableAmountType {
    override val value: String = "SUPPLY_WITH_VAT"
  }
  private object SupplyWithVatSerializer : KSerializer<SupplyWithVat> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SupplyWithVat::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SupplyWithVat = decoder.decodeString().let {
      if (it != "SUPPLY_WITH_VAT") {
        throw SerializationException(it)
      } else {
        return SupplyWithVat
      }
    }
    override fun serialize(encoder: Encoder, value: SupplyWithVat) = encoder.encodeString(value.value)
  }
  /** 면세 금액 */
  @Serializable(TaxFreeSerializer::class)
  public data object TaxFree : PlatformCancellableAmountType {
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
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformCancellableAmountType
}


private object PlatformCancellableAmountTypeSerializer : KSerializer<PlatformCancellableAmountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformCancellableAmountType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformCancellableAmountType {
    val value = decoder.decodeString()
    return when (value) {
      "SUPPLY_WITH_VAT" -> PlatformCancellableAmountType.SupplyWithVat
      "TAX_FREE" -> PlatformCancellableAmountType.TaxFree
      else -> PlatformCancellableAmountType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformCancellableAmountType) = encoder.encodeString(value.value)
}
