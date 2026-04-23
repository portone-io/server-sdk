package io.portone.sdk.server.pgspecific

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 페이먼트월 배송 상태 */
@Serializable(PaymentwallDeliveryStatusSerializer::class)
public sealed interface PaymentwallDeliveryStatus {
  public val value: String
  /** 주문 접수 */
  @Serializable(OrderPlacedSerializer::class)
  public data object OrderPlaced : PaymentwallDeliveryStatus {
    override val value: String = "ORDER_PLACED"
  }
  public object OrderPlacedSerializer : KSerializer<OrderPlaced> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(OrderPlaced::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): OrderPlaced = decoder.decodeString().let {
      if (it != "ORDER_PLACED") {
        throw SerializationException(it)
      } else {
        return OrderPlaced
      }
    }
    override fun serialize(encoder: Encoder, value: OrderPlaced): Unit = encoder.encodeString(value.value)
  }
  /** 배송 중 */
  @Serializable(OrderShippedSerializer::class)
  public data object OrderShipped : PaymentwallDeliveryStatus {
    override val value: String = "ORDER_SHIPPED"
  }
  public object OrderShippedSerializer : KSerializer<OrderShipped> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(OrderShipped::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): OrderShipped = decoder.decodeString().let {
      if (it != "ORDER_SHIPPED") {
        throw SerializationException(it)
      } else {
        return OrderShipped
      }
    }
    override fun serialize(encoder: Encoder, value: OrderShipped): Unit = encoder.encodeString(value.value)
  }
  /** 배송 완료 */
  @Serializable(DeliveredSerializer::class)
  public data object Delivered : PaymentwallDeliveryStatus {
    override val value: String = "DELIVERED"
  }
  public object DeliveredSerializer : KSerializer<Delivered> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Delivered::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Delivered = decoder.decodeString().let {
      if (it != "DELIVERED") {
        throw SerializationException(it)
      } else {
        return Delivered
      }
    }
    override fun serialize(encoder: Encoder, value: Delivered): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentwallDeliveryStatus
}


public object PaymentwallDeliveryStatusSerializer : KSerializer<PaymentwallDeliveryStatus> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentwallDeliveryStatus::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentwallDeliveryStatus {
    val value = decoder.decodeString()
    return when (value) {
      "ORDER_PLACED" -> PaymentwallDeliveryStatus.OrderPlaced
      "ORDER_SHIPPED" -> PaymentwallDeliveryStatus.OrderShipped
      "DELIVERED" -> PaymentwallDeliveryStatus.Delivered
      else -> PaymentwallDeliveryStatus.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentwallDeliveryStatus): Unit = encoder.encodeString(value.value)
}
