package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 가상계좌 유형 */
@Serializable(PaymentMethodVirtualAccountTypeSerializer::class)
public sealed interface PaymentMethodVirtualAccountType {
  public val value: String
  /** 고정식 */
  @Serializable(FixedSerializer::class)
  public data object Fixed : PaymentMethodVirtualAccountType {
    override val value: String = "FIXED"
  }
  public object FixedSerializer : KSerializer<Fixed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fixed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fixed = decoder.decodeString().let {
      if (it != "FIXED") {
        throw SerializationException(it)
      } else {
        return Fixed
      }
    }
    override fun serialize(encoder: Encoder, value: Fixed): Unit = encoder.encodeString(value.value)
  }
  /** 회전식 */
  @Serializable(NormalSerializer::class)
  public data object Normal : PaymentMethodVirtualAccountType {
    override val value: String = "NORMAL"
  }
  public object NormalSerializer : KSerializer<Normal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Normal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Normal = decoder.decodeString().let {
      if (it != "NORMAL") {
        throw SerializationException(it)
      } else {
        return Normal
      }
    }
    override fun serialize(encoder: Encoder, value: Normal): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodVirtualAccountType
}


public object PaymentMethodVirtualAccountTypeSerializer : KSerializer<PaymentMethodVirtualAccountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodVirtualAccountType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodVirtualAccountType {
    val value = decoder.decodeString()
    return when (value) {
      "FIXED" -> PaymentMethodVirtualAccountType.Fixed
      "NORMAL" -> PaymentMethodVirtualAccountType.Normal
      else -> PaymentMethodVirtualAccountType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodVirtualAccountType): Unit = encoder.encodeString(value.value)
}
