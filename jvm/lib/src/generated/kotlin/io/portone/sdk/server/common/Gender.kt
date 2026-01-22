package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 성별 */
@Serializable(GenderSerializer::class)
public sealed interface Gender {
  public val value: String
  /** 남성 */
  @Serializable(MaleSerializer::class)
  public data object Male : Gender {
    override val value: String = "MALE"
  }
  public object MaleSerializer : KSerializer<Male> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Male::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Male = decoder.decodeString().let {
      if (it != "MALE") {
        throw SerializationException(it)
      } else {
        return Male
      }
    }
    override fun serialize(encoder: Encoder, value: Male): Unit = encoder.encodeString(value.value)
  }
  /** 여성 */
  @Serializable(FemaleSerializer::class)
  public data object Female : Gender {
    override val value: String = "FEMALE"
  }
  public object FemaleSerializer : KSerializer<Female> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Female::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Female = decoder.decodeString().let {
      if (it != "FEMALE") {
        throw SerializationException(it)
      } else {
        return Female
      }
    }
    override fun serialize(encoder: Encoder, value: Female): Unit = encoder.encodeString(value.value)
  }
  /** 그 외 성별 */
  @Serializable(OtherSerializer::class)
  public data object Other : Gender {
    override val value: String = "OTHER"
  }
  public object OtherSerializer : KSerializer<Other> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Other::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Other = decoder.decodeString().let {
      if (it != "OTHER") {
        throw SerializationException(it)
      } else {
        return Other
      }
    }
    override fun serialize(encoder: Encoder, value: Other): Unit = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Gender
}


public object GenderSerializer : KSerializer<Gender> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gender::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Gender {
    val value = decoder.decodeString()
    return when (value) {
      "MALE" -> Gender.Male
      "FEMALE" -> Gender.Female
      "OTHER" -> Gender.Other
      else -> Gender.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Gender): Unit = encoder.encodeString(value.value)
}
