package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Fixed : PaymentMethodVirtualAccountType {
    override val value: String = "FIXED"
  }
  /** 회전식 */
  public data object Normal : PaymentMethodVirtualAccountType {
    override val value: String = "NORMAL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentMethodVirtualAccountType
}


private object PaymentMethodVirtualAccountTypeSerializer : KSerializer<PaymentMethodVirtualAccountType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentMethodVirtualAccountType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentMethodVirtualAccountType {
    val value = decoder.decodeString()
    return when (value) {
      "FIXED" -> PaymentMethodVirtualAccountType.Fixed
      "NORMAL" -> PaymentMethodVirtualAccountType.Normal
      else -> PaymentMethodVirtualAccountType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentMethodVirtualAccountType) = encoder.encodeString(value.value)
}
