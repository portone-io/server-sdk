package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 정산 유형 */
@Serializable(PlatformPartnerSettlementTypeSerializer::class)
public sealed interface PlatformPartnerSettlementType {
  public val value: String
  /** 수동 정산 */
  public data object Manual : PlatformPartnerSettlementType {
    override val value: String = "MANUAL"
  }
  /** 주문 정산 */
  public data object Order : PlatformPartnerSettlementType {
    override val value: String = "ORDER"
  }
  /** 주문 취소 정산 */
  public data object OrderCancel : PlatformPartnerSettlementType {
    override val value: String = "ORDER_CANCEL"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerSettlementType
}


private object PlatformPartnerSettlementTypeSerializer : KSerializer<PlatformPartnerSettlementType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerSettlementType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPartnerSettlementType {
    val value = decoder.decodeString()
    return when (value) {
      "MANUAL" -> PlatformPartnerSettlementType.Manual
      "ORDER" -> PlatformPartnerSettlementType.Order
      "ORDER_CANCEL" -> PlatformPartnerSettlementType.OrderCancel
      else -> PlatformPartnerSettlementType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPartnerSettlementType) = encoder.encodeString(value.value)
}
