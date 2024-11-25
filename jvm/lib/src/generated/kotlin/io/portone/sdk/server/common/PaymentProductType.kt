package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 상품 유형 */
@Serializable(PaymentProductTypeSerializer::class)
public sealed interface PaymentProductType {
  public val value: String
  /** 실물 상품 */
  public data object Physical : PaymentProductType {
    override val value: String = "PHYSICAL"
  }
  /**
   * 디지털 상품
   *
   * 서비스, 온라인 상품 등 실물이 존재하지 않는 무형의 상품을 의미합니다.
   */
  public data object Digital : PaymentProductType {
    override val value: String = "DIGITAL"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentProductType
}


private object PaymentProductTypeSerializer : KSerializer<PaymentProductType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentProductType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentProductType {
    val value = decoder.decodeString()
    return when (value) {
      "PHYSICAL" -> PaymentProductType.Physical
      "DIGITAL" -> PaymentProductType.Digital
      else -> PaymentProductType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentProductType) = encoder.encodeString(value.value)
}
