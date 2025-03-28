package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 요일 */
@Serializable(DayOfWeekSerializer::class)
public sealed interface DayOfWeek {
  public val value: String
  @Serializable(SunSerializer::class)
  public data object Sun : DayOfWeek {
    override val value: String = "SUN"
  }
  private object SunSerializer : KSerializer<Sun> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sun::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sun = decoder.decodeString().let {
      if (it != "SUN") {
        throw SerializationException(it)
      } else {
        return Sun
      }
    }
    override fun serialize(encoder: Encoder, value: Sun) = encoder.encodeString(value.value)
  }
  @Serializable(MonSerializer::class)
  public data object Mon : DayOfWeek {
    override val value: String = "MON"
  }
  private object MonSerializer : KSerializer<Mon> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Mon::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Mon = decoder.decodeString().let {
      if (it != "MON") {
        throw SerializationException(it)
      } else {
        return Mon
      }
    }
    override fun serialize(encoder: Encoder, value: Mon) = encoder.encodeString(value.value)
  }
  @Serializable(TueSerializer::class)
  public data object Tue : DayOfWeek {
    override val value: String = "TUE"
  }
  private object TueSerializer : KSerializer<Tue> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Tue::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Tue = decoder.decodeString().let {
      if (it != "TUE") {
        throw SerializationException(it)
      } else {
        return Tue
      }
    }
    override fun serialize(encoder: Encoder, value: Tue) = encoder.encodeString(value.value)
  }
  @Serializable(WedSerializer::class)
  public data object Wed : DayOfWeek {
    override val value: String = "WED"
  }
  private object WedSerializer : KSerializer<Wed> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Wed::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Wed = decoder.decodeString().let {
      if (it != "WED") {
        throw SerializationException(it)
      } else {
        return Wed
      }
    }
    override fun serialize(encoder: Encoder, value: Wed) = encoder.encodeString(value.value)
  }
  @Serializable(ThuSerializer::class)
  public data object Thu : DayOfWeek {
    override val value: String = "THU"
  }
  private object ThuSerializer : KSerializer<Thu> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Thu::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Thu = decoder.decodeString().let {
      if (it != "THU") {
        throw SerializationException(it)
      } else {
        return Thu
      }
    }
    override fun serialize(encoder: Encoder, value: Thu) = encoder.encodeString(value.value)
  }
  @Serializable(FriSerializer::class)
  public data object Fri : DayOfWeek {
    override val value: String = "FRI"
  }
  private object FriSerializer : KSerializer<Fri> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Fri::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Fri = decoder.decodeString().let {
      if (it != "FRI") {
        throw SerializationException(it)
      } else {
        return Fri
      }
    }
    override fun serialize(encoder: Encoder, value: Fri) = encoder.encodeString(value.value)
  }
  @Serializable(SatSerializer::class)
  public data object Sat : DayOfWeek {
    override val value: String = "SAT"
  }
  private object SatSerializer : KSerializer<Sat> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(Sat::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): Sat = decoder.decodeString().let {
      if (it != "SAT") {
        throw SerializationException(it)
      } else {
        return Sat
      }
    }
    override fun serialize(encoder: Encoder, value: Sat) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  public data class Unrecognized internal constructor(override val value: String) : DayOfWeek
}


private object DayOfWeekSerializer : KSerializer<DayOfWeek> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(DayOfWeek::class.java.name, PrimitiveKind.STRING)
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
