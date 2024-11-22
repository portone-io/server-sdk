package io.portone.sdk.server.common

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object Male : Gender {
    override val value: String = "MALE"
  }
  /** 여성 */
  public data object Female : Gender {
    override val value: String = "FEMALE"
  }
  /** 그 외 성별 */
  public data object Other : Gender {
    override val value: String = "OTHER"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : Gender
}


private object GenderSerializer : KSerializer<Gender> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Gender::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): Gender {
    val value = decoder.decodeString()
    return when (value) {
      "MALE" -> Gender.Male
      "FEMALE" -> Gender.Female
      "OTHER" -> Gender.Other
      else -> Gender.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: Gender) = encoder.encodeString(value.value)
}
