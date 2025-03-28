package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 결제가 발생한 클라이언트 환경 */
@Serializable(PaymentClientTypeSerializer::class)
public sealed interface PaymentClientType {
  public val value: String
  @Serializable(SdkMobileSerializer::class)
  public data object SdkMobile : PaymentClientType {
    override val value: String = "SDK_MOBILE"
  }
  private object SdkMobileSerializer : KSerializer<SdkMobile> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SdkMobile::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SdkMobile = decoder.decodeString().let {
      if (it != "SDK_MOBILE") {
        throw SerializationException(it)
      } else {
        return SdkMobile
      }
    }
    override fun serialize(encoder: Encoder, value: SdkMobile) = encoder.encodeString(value.value)
  }
  @Serializable(SdkPcSerializer::class)
  public data object SdkPc : PaymentClientType {
    override val value: String = "SDK_PC"
  }
  private object SdkPcSerializer : KSerializer<SdkPc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SdkPc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): SdkPc = decoder.decodeString().let {
      if (it != "SDK_PC") {
        throw SerializationException(it)
      } else {
        return SdkPc
      }
    }
    override fun serialize(encoder: Encoder, value: SdkPc) = encoder.encodeString(value.value)
  }
  @Serializable(ApiSerializer::class)
  public data object Api : PaymentClientType {
    override val value: String = "API"
  }
  private object ApiSerializer : KSerializer<Api> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Api::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Api = decoder.decodeString().let {
      if (it != "API") {
        throw SerializationException(it)
      } else {
        return Api
      }
    }
    override fun serialize(encoder: Encoder, value: Api) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : PaymentClientType
}


private object PaymentClientTypeSerializer : KSerializer<PaymentClientType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentClientType::class.java.name, PrimitiveKind.STRING)
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
