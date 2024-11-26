package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 금액에 대한 소수점 처리 방식 */
@Serializable(PlatformRoundTypeSerializer::class)
public sealed interface PlatformRoundType {
  public val value: String
  /** 소수점 반올림 */
  @Serializable(OffSerializer::class)
  public data object Off : PlatformRoundType {
    override val value: String = "OFF"
  }
  private object OffSerializer : KSerializer<Off> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Off::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Off = decoder.decodeString().let {
      if (it != "OFF") {
        throw SerializationException(it)
      } else {
        return Off
      }
    }
    override fun serialize(encoder: Encoder, value: Off) = encoder.encodeString(value.value)
  }
  /** 소수점 내림 */
  @Serializable(DownSerializer::class)
  public data object Down : PlatformRoundType {
    override val value: String = "DOWN"
  }
  private object DownSerializer : KSerializer<Down> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Down::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Down = decoder.decodeString().let {
      if (it != "DOWN") {
        throw SerializationException(it)
      } else {
        return Down
      }
    }
    override fun serialize(encoder: Encoder, value: Down) = encoder.encodeString(value.value)
  }
  /** 소수점 올림 */
  @Serializable(UpSerializer::class)
  public data object Up : PlatformRoundType {
    override val value: String = "UP"
  }
  private object UpSerializer : KSerializer<Up> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Up::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Up = decoder.decodeString().let {
      if (it != "UP") {
        throw SerializationException(it)
      } else {
        return Up
      }
    }
    override fun serialize(encoder: Encoder, value: Up) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformRoundType
}


private object PlatformRoundTypeSerializer : KSerializer<PlatformRoundType> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformRoundType::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformRoundType {
    val value = decoder.decodeString()
    return when (value) {
      "OFF" -> PlatformRoundType.Off
      "DOWN" -> PlatformRoundType.Down
      "UP" -> PlatformRoundType.Up
      else -> PlatformRoundType.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformRoundType) = encoder.encodeString(value.value)
}
