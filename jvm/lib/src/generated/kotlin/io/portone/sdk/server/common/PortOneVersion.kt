package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 포트원 버전 */
@Serializable(PortOneVersionSerializer::class)
public sealed interface PortOneVersion {
  public val value: String
  @Serializable(V1Serializer::class)
  public data object V1 : PortOneVersion {
    override val value: String = "V1"
  }
  private object V1Serializer : KSerializer<V1> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(V1::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): V1 = decoder.decodeString().let {
      if (it != "V1") {
        throw SerializationException(it)
      } else {
        return V1
      }
    }
    override fun serialize(encoder: Encoder, value: V1) = encoder.encodeString(value.value)
  }
  @Serializable(V2Serializer::class)
  public data object V2 : PortOneVersion {
    override val value: String = "V2"
  }
  private object V2Serializer : KSerializer<V2> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(V2::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): V2 = decoder.decodeString().let {
      if (it != "V2") {
        throw SerializationException(it)
      } else {
        return V2
      }
    }
    override fun serialize(encoder: Encoder, value: V2) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PortOneVersion
}


private object PortOneVersionSerializer : KSerializer<PortOneVersion> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PortOneVersion::class.java.name, PrimitiveKind.STRING)
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
