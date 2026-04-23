package io.portone.sdk.server.payment

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 타입 */
@Serializable(PaymentOriginPlatformTypeSerializer::class)
public sealed interface PaymentOriginPlatformType {
  public val value: String
  @Serializable(PcSerializer::class)
  public data object Pc : PaymentOriginPlatformType {
    override val value: String = "PC"
  }
  public object PcSerializer : KSerializer<Pc> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Pc::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Pc = decoder.decodeString().let {
      if (it != "PC") {
        throw SerializationException(it)
      } else {
        return Pc
      }
    }
    override fun serialize(encoder: Encoder, value: Pc): Unit = encoder.encodeString(value.value)
  }
  @Serializable(MobileSerializer::class)
  public data object Mobile : PaymentOriginPlatformType {
    override val value: String = "MOBILE"
  }
  public object MobileSerializer : KSerializer<Mobile> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mobile::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mobile = decoder.decodeString().let {
      if (it != "MOBILE") {
        throw SerializationException(it)
      } else {
        return Mobile
      }
    }
    override fun serialize(encoder: Encoder, value: Mobile): Unit = encoder.encodeString(value.value)
  }
  @Serializable(ApiSerializer::class)
  public data object Api : PaymentOriginPlatformType {
    override val value: String = "API"
  }
  public object ApiSerializer : KSerializer<Api> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Api::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Api = decoder.decodeString().let {
      if (it != "API") {
        throw SerializationException(it)
      } else {
        return Api
      }
    }
    override fun serialize(encoder: Encoder, value: Api): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PaymentOriginPlatformType
}


public object PaymentOriginPlatformTypeSerializer : KSerializer<PaymentOriginPlatformType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PaymentOriginPlatformType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PaymentOriginPlatformType {
    val value = decoder.decodeString()
    return when (value) {
      "PC" -> PaymentOriginPlatformType.Pc
      "MOBILE" -> PaymentOriginPlatformType.Mobile
      "API" -> PaymentOriginPlatformType.Api
      else -> PaymentOriginPlatformType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PaymentOriginPlatformType): Unit = encoder.encodeString(value.value)
}
