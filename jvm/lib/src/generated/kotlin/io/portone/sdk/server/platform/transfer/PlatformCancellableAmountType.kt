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
@Serializable(PlatformCancellableAmountTypeSerializer::class)
public sealed interface PlatformCancellableAmountType {
  public val value: String
  /**
   * 공급대가
   *
   * 공급가액과 부가세를 더한 금액입니다.
   */
  public data object SupplyWithVat : PlatformCancellableAmountType {
    override val value: String = "SUPPLY_WITH_VAT"
  }
  /** 면세 금액 */
  public data object TaxFree : PlatformCancellableAmountType {
    override val value: String = "TAX_FREE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformCancellableAmountType
}


private object PlatformCancellableAmountTypeSerializer : KSerializer<PlatformCancellableAmountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformCancellableAmountType::class.java.canonicalName, PrimitiveKind.STRING)
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
