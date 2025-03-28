package io.portone.sdk.server.platform.partnersettlement

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(ManualSerializer::class)
  public data object Manual : PlatformPartnerSettlementType {
    override val value: String = "MANUAL"
  }
  private object ManualSerializer : KSerializer<Manual> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Manual::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Manual = decoder.decodeString().let {
      if (it != "MANUAL") {
        throw SerializationException(it)
      } else {
        return Manual
      }
    }
    override fun serialize(encoder: Encoder, value: Manual) = encoder.encodeString(value.value)
  }
  /** 주문 정산 */
  @Serializable(OrderSerializer::class)
  public data object Order : PlatformPartnerSettlementType {
    override val value: String = "ORDER"
  }
  private object OrderSerializer : KSerializer<Order> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Order::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Order = decoder.decodeString().let {
      if (it != "ORDER") {
        throw SerializationException(it)
      } else {
        return Order
      }
    }
    override fun serialize(encoder: Encoder, value: Order) = encoder.encodeString(value.value)
  }
  /** 주문 취소 정산 */
  @Serializable(OrderCancelSerializer::class)
  public data object OrderCancel : PlatformPartnerSettlementType {
    override val value: String = "ORDER_CANCEL"
  }
  private object OrderCancelSerializer : KSerializer<OrderCancel> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(OrderCancel::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): OrderCancel = decoder.decodeString().let {
      if (it != "ORDER_CANCEL") {
        throw SerializationException(it)
      } else {
        return OrderCancel
      }
    }
    override fun serialize(encoder: Encoder, value: OrderCancel) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PlatformPartnerSettlementType
}


private object PlatformPartnerSettlementTypeSerializer : KSerializer<PlatformPartnerSettlementType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPartnerSettlementType::class.java.name, PrimitiveKind.STRING)
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
