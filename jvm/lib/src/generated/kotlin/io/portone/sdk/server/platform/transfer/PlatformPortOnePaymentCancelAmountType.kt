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
@Serializable(PlatformPortOnePaymentCancelAmountTypeSerializer::class)
public sealed interface PlatformPortOnePaymentCancelAmountType {
  public val value: String
  /**
   * 공급대가
   *
   * 공급가액과 부가세를 더한 금액입니다.
   */
  @Serializable(SupplyWithVatSerializer::class)
  public data object SupplyWithVat : PlatformPortOnePaymentCancelAmountType {
    override val value: String = "SUPPLY_WITH_VAT"
  }
  public object SupplyWithVatSerializer : KSerializer<SupplyWithVat> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SupplyWithVat::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SupplyWithVat = decoder.decodeString().let {
      if (it != "SUPPLY_WITH_VAT") {
        throw SerializationException(it)
      } else {
        return SupplyWithVat
      }
    }
    override fun serialize(encoder: Encoder, value: SupplyWithVat): Unit = encoder.encodeString(value.value)
  }
  /** 면세 금액 */
  @Serializable(TaxFreeSerializer::class)
  public data object TaxFree : PlatformPortOnePaymentCancelAmountType {
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
  public data class Unrecognized internal constructor(override val value: String) : PlatformPortOnePaymentCancelAmountType
}


public object PlatformPortOnePaymentCancelAmountTypeSerializer : KSerializer<PlatformPortOnePaymentCancelAmountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPortOnePaymentCancelAmountType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPortOnePaymentCancelAmountType {
    val value = decoder.decodeString()
    return when (value) {
      "SUPPLY_WITH_VAT" -> PlatformPortOnePaymentCancelAmountType.SupplyWithVat
      "TAX_FREE" -> PlatformPortOnePaymentCancelAmountType.TaxFree
      else -> PlatformPortOnePaymentCancelAmountType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPortOnePaymentCancelAmountType): Unit = encoder.encodeString(value.value)
}
