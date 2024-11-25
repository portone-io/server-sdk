package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 포트원 버전 */
@Serializable(PortOneVersionSerializer::class)
public sealed interface PortOneVersion {
  public val value: String
  public data object V1 : PortOneVersion {
    override val value: String = "V1"
  }
  public data object V2 : PortOneVersion {
    override val value: String = "V2"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PortOneVersion
}


private object PortOneVersionSerializer : KSerializer<PortOneVersion> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PortOneVersion::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PortOneVersion {
    val value = decoder.decodeString()
    return when (value) {
      "V1" -> PortOneVersion.V1
      "V2" -> PortOneVersion.V2
      else -> PortOneVersion.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PortOneVersion) = encoder.encodeString(value.value)
}
