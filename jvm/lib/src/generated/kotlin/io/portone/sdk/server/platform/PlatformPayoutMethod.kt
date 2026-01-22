package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformPayoutMethodSerializer::class)
public sealed interface PlatformPayoutMethod {
  public val value: String
  @Serializable(DirectSerializer::class)
  public data object Direct : PlatformPayoutMethod {
    override val value: String = "DIRECT"
  }
  public object DirectSerializer : KSerializer<Direct> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Direct::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Direct = decoder.decodeString().let {
      if (it != "DIRECT") {
        throw SerializationException(it)
      } else {
        return Direct
      }
    }
    override fun serialize(encoder: Encoder, value: Direct): Unit = encoder.encodeString(value.value)
  }
  @Serializable(AgencySerializer::class)
  public data object Agency : PlatformPayoutMethod {
    override val value: String = "AGENCY"
  }
  public object AgencySerializer : KSerializer<Agency> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Agency::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Agency = decoder.decodeString().let {
      if (it != "AGENCY") {
        throw SerializationException(it)
      } else {
        return Agency
      }
    }
    override fun serialize(encoder: Encoder, value: Agency): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutMethod
}


public object PlatformPayoutMethodSerializer : KSerializer<PlatformPayoutMethod> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayoutMethod::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayoutMethod {
    val value = decoder.decodeString()
    return when (value) {
      "DIRECT" -> PlatformPayoutMethod.Direct
      "AGENCY" -> PlatformPayoutMethod.Agency
      else -> PlatformPayoutMethod.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayoutMethod): Unit = encoder.encodeString(value.value)
}
