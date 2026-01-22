package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformTransferTypeSerializer::class)
public sealed interface PlatformTransferType {
  public val value: String
  @Serializable(OrderSerializer::class)
  public data object Order : PlatformTransferType {
    override val value: String = "ORDER"
  }
  public object OrderSerializer : KSerializer<Order> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Order::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Order = decoder.decodeString().let {
      if (it != "ORDER") {
        throw SerializationException(it)
      } else {
        return Order
      }
    }
    override fun serialize(encoder: Encoder, value: Order): Unit = encoder.encodeString(value.value)
  }
  @Serializable(OrderCancelSerializer::class)
  public data object OrderCancel : PlatformTransferType {
    override val value: String = "ORDER_CANCEL"
  }
  public object OrderCancelSerializer : KSerializer<OrderCancel> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(OrderCancel::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): OrderCancel = decoder.decodeString().let {
      if (it != "ORDER_CANCEL") {
        throw SerializationException(it)
      } else {
        return OrderCancel
      }
    }
    override fun serialize(encoder: Encoder, value: OrderCancel): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ManualSerializer::class)
  public data object Manual : PlatformTransferType {
    override val value: String = "MANUAL"
  }
  public object ManualSerializer : KSerializer<Manual> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Manual::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Manual = decoder.decodeString().let {
      if (it != "MANUAL") {
        throw SerializationException(it)
      } else {
        return Manual
      }
    }
    override fun serialize(encoder: Encoder, value: Manual): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferType
}


public object PlatformTransferTypeSerializer : KSerializer<PlatformTransferType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformTransferType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformTransferType {
    val value = decoder.decodeString()
    return when (value) {
      "ORDER" -> PlatformTransferType.Order
      "ORDER_CANCEL" -> PlatformTransferType.OrderCancel
      "MANUAL" -> PlatformTransferType.Manual
      else -> PlatformTransferType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformTransferType): Unit = encoder.encodeString(value.value)
}
