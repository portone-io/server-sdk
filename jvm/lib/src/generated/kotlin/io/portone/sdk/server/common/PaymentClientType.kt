package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제가 발생한 클라이언트 환경 */
@Serializable(PaymentClientTypeSerializer::class)
public sealed interface PaymentClientType {
  public val value: String
  public data object SdkMobile : PaymentClientType {
    override val value: String = "SDK_MOBILE"
  }
  public data object SdkPc : PaymentClientType {
    override val value: String = "SDK_PC"
  }
  public data object Api : PaymentClientType {
    override val value: String = "API"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentClientType
}


private object PaymentClientTypeSerializer : KSerializer<PaymentClientType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentClientType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentClientType {
    val value = decoder.decodeString()
    return when (value) {
      "SDK_MOBILE" -> PaymentClientType.SdkMobile
      "SDK_PC" -> PaymentClientType.SdkPc
      "API" -> PaymentClientType.Api
      else -> PaymentClientType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentClientType) = encoder.encodeString(value.value)
}
