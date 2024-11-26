package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 가상계좌 발급 유형 */
@Serializable(InstantPaymentMethodInputVirtualAccountOptionTypeSerializer::class)
public sealed interface InstantPaymentMethodInputVirtualAccountOptionType {
  public val value: String
  /**
   * 회전식 가상계좌
   *
   * 일반적으로 사용되는 방식이며 PG사에서 직접 채번한 가상계좌번호를 사용합니다.
   */
  @Serializable(NormalSerializer::class)
  public data object Normal : InstantPaymentMethodInputVirtualAccountOptionType {
    override val value: String = "NORMAL"
  }
  private object NormalSerializer : KSerializer<Normal> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Normal::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Normal = decoder.decodeString().let {
      if (it != "NORMAL") {
        throw SerializationException(it)
      } else {
        return Normal
      }
    }
    override fun serialize(encoder: Encoder, value: Normal) = encoder.encodeString(value.value)
  }
  /** 고정식 가상계좌 */
  @Serializable(FixedSerializer::class)
  public data object Fixed : InstantPaymentMethodInputVirtualAccountOptionType {
    override val value: String = "FIXED"
  }
  private object FixedSerializer : KSerializer<Fixed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fixed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fixed = decoder.decodeString().let {
      if (it != "FIXED") {
        throw SerializationException(it)
      } else {
        return Fixed
      }
    }
    override fun serialize(encoder: Encoder, value: Fixed) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : InstantPaymentMethodInputVirtualAccountOptionType
}


private object InstantPaymentMethodInputVirtualAccountOptionTypeSerializer : KSerializer<InstantPaymentMethodInputVirtualAccountOptionType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(InstantPaymentMethodInputVirtualAccountOptionType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): InstantPaymentMethodInputVirtualAccountOptionType {
    val value = decoder.decodeString()
    return when (value) {
      "NORMAL" -> InstantPaymentMethodInputVirtualAccountOptionType.Normal
      "FIXED" -> InstantPaymentMethodInputVirtualAccountOptionType.Fixed
      else -> InstantPaymentMethodInputVirtualAccountOptionType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: InstantPaymentMethodInputVirtualAccountOptionType) = encoder.encodeString(value.value)
}
