package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

@Serializable(PlatformPayoutMethodSerializer::class)
public sealed interface PlatformPayoutMethod {
  public val value: String
  public data object Direct : PlatformPayoutMethod {
    override val value: String = "DIRECT"
  }
  public data object Agency : PlatformPayoutMethod {
    override val value: String = "AGENCY"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutMethod
}


private object PlatformPayoutMethodSerializer : KSerializer<PlatformPayoutMethod> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformPayoutMethod::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformPayoutMethod {
    val value = decoder.decodeString()
    return when (value) {
      "DIRECT" -> PlatformPayoutMethod.Direct
      "AGENCY" -> PlatformPayoutMethod.Agency
      else -> PlatformPayoutMethod.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformPayoutMethod) = encoder.encodeString(value.value)
}
