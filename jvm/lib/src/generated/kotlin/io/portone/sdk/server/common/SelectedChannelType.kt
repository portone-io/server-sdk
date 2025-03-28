package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
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
  @Serializable(LiveSerializer::class)
  public data object Live : SelectedChannelType {
    override val value: String = "LIVE"
  }
  private object LiveSerializer : KSerializer<Live> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Live::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Live = decoder.decodeString().let {
      if (it != "LIVE") {
        throw SerializationException(it)
      } else {
        return Live
      }
    }
    override fun serialize(encoder: Encoder, value: Live) = encoder.encodeString(value.value)
  }
  /** 테스트 연동 채널 */
  @Serializable(TestSerializer::class)
  public data object Test : SelectedChannelType {
    override val value: String = "TEST"
  }
  private object TestSerializer : KSerializer<Test> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Test::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Test = decoder.decodeString().let {
      if (it != "TEST") {
        throw SerializationException(it)
      } else {
        return Test
      }
    }
    override fun serialize(encoder: Encoder, value: Test) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : SelectedChannelType
}


private object SelectedChannelTypeSerializer : KSerializer<SelectedChannelType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(SelectedChannelType::class.java.name, PrimitiveKind.STRING)
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
