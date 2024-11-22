package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object SupplyWithVat : PlatformPortOnePaymentCancelAmountType {
    override val value: String = "SUPPLY_WITH_VAT"
  }
  /** 면세 금액 */
  public data object TaxFree : PlatformPortOnePaymentCancelAmountType {
    override val value: String = "TAX_FREE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPortOnePaymentCancelAmountType
}


private object PlatformPortOnePaymentCancelAmountTypeSerializer : KSerializer<PlatformPortOnePaymentCancelAmountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPortOnePaymentCancelAmountType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPortOnePaymentCancelAmountType {
    val value = decoder.decodeString()
    return when (value) {
      "SUPPLY_WITH_VAT" -> PlatformPortOnePaymentCancelAmountType.SupplyWithVat
      "TAX_FREE" -> PlatformPortOnePaymentCancelAmountType.TaxFree
      else -> PlatformPortOnePaymentCancelAmountType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPortOnePaymentCancelAmountType) = encoder.encodeString(value.value)
}
