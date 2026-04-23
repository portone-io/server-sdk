package io.portone.sdk.server.pgspecific

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 페이먼트월 배송 유형 */
@Serializable(PaymentwallDeliveryTypeSerializer::class)
public sealed interface PaymentwallDeliveryType {
  public val value: String
  /** 디지털 */
  @Serializable(DigitalSerializer::class)
  public data object Digital : PaymentwallDeliveryType {
    override val value: String = "DIGITAL"
  }
  public object DigitalSerializer : KSerializer<Digital> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Digital::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Digital = decoder.decodeString().let {
      if (it != "DIGITAL") {
        throw SerializationException(it)
      } else {
        return Digital
      }
    }
    override fun serialize(encoder: Encoder, value: Digital): Unit = encoder.encodeString(value.value)
  }
  /** 실물 */
  @Serializable(PhysicalSerializer::class)
  public data object Physical : PaymentwallDeliveryType {
    override val value: String = "PHYSICAL"
  }
  public object PhysicalSerializer : KSerializer<Physical> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Physical::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Physical = decoder.decodeString().let {
      if (it != "PHYSICAL") {
        throw SerializationException(it)
      } else {
        return Physical
      }
    }
    override fun serialize(encoder: Encoder, value: Physical): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentwallDeliveryType
}


public object PaymentwallDeliveryTypeSerializer : KSerializer<PaymentwallDeliveryType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentwallDeliveryType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentwallDeliveryType {
    val value = decoder.decodeString()
    return when (value) {
      "DIGITAL" -> PaymentwallDeliveryType.Digital
      "PHYSICAL" -> PaymentwallDeliveryType.Physical
      else -> PaymentwallDeliveryType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentwallDeliveryType): Unit = encoder.encodeString(value.value)
}
