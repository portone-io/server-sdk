package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 채널 타입 */
@Serializable(SelectedChannelTypeSerializer::class)
public sealed interface SelectedChannelType {
  public val value: String
  /** 실 연동 채널 */
  public data object Live : SelectedChannelType {
    override val value: String = "LIVE"
  }
  /** 테스트 연동 채널 */
  public data object Test : SelectedChannelType {
    override val value: String = "TEST"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : SelectedChannelType
}


private object SelectedChannelTypeSerializer : KSerializer<SelectedChannelType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SelectedChannelType::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): SelectedChannelType {
    val value = decoder.decodeString()
    return when (value) {
      "LIVE" -> SelectedChannelType.Live
      "TEST" -> SelectedChannelType.Test
      else -> SelectedChannelType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: SelectedChannelType) = encoder.encodeString(value.value)
}
