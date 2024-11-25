package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 요일 */
@Serializable(DayOfWeekSerializer::class)
public sealed interface DayOfWeek {
  public val value: String
  public data object Sun : DayOfWeek {
    override val value: String = "SUN"
  }
  public data object Mon : DayOfWeek {
    override val value: String = "MON"
  }
  public data object Tue : DayOfWeek {
    override val value: String = "TUE"
  }
  public data object Wed : DayOfWeek {
    override val value: String = "WED"
  }
  public data object Thu : DayOfWeek {
    override val value: String = "THU"
  }
  public data object Fri : DayOfWeek {
    override val value: String = "FRI"
  }
  public data object Sat : DayOfWeek {
    override val value: String = "SAT"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : DayOfWeek
}


private object DayOfWeekSerializer : KSerializer<DayOfWeek> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DayOfWeek::class.java.canonicalName, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): DayOfWeek {
    val value = decoder.decodeString()
    return when (value) {
      "SUN" -> DayOfWeek.Sun
      "MON" -> DayOfWeek.Mon
      "TUE" -> DayOfWeek.Tue
      "WED" -> DayOfWeek.Wed
      "THU" -> DayOfWeek.Thu
      "FRI" -> DayOfWeek.Fri
      "SAT" -> DayOfWeek.Sat
      else -> DayOfWeek.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: DayOfWeek) = encoder.encodeString(value.value)
}
