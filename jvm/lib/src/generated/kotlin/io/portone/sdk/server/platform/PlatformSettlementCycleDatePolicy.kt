package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.SerializationException
import kotlinx.serialization.descriptors.PrimitiveKind
import kotlinx.serialization.descriptors.PrimitiveSerialDescriptor
import kotlinx.serialization.descriptors.SerialDescriptor
import kotlinx.serialization.encoding.Decoder
import kotlinx.serialization.encoding.Encoder

/** 플랫폼 정산 기준일 */
@Serializable(PlatformSettlementCycleDatePolicySerializer::class)
public sealed interface PlatformSettlementCycleDatePolicy {
  public val value: String
  /** 공휴일 전 영업일 */
  @Serializable(HolidayBeforeSerializer::class)
  public data object HolidayBefore : PlatformSettlementCycleDatePolicy {
    override val value: String = "HOLIDAY_BEFORE"
  }
  private object HolidayBeforeSerializer : KSerializer<HolidayBefore> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HolidayBefore::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HolidayBefore = decoder.decodeString().let {
      if (it != "HOLIDAY_BEFORE") {
        throw SerializationException(it)
      } else {
        return HolidayBefore
      }
    }
    override fun serialize(encoder: Encoder, value: HolidayBefore) = encoder.encodeString(value.value)
  }
  /** 공휴일 후 영업일 */
  @Serializable(HolidayAfterSerializer::class)
  public data object HolidayAfter : PlatformSettlementCycleDatePolicy {
    override val value: String = "HOLIDAY_AFTER"
  }
  private object HolidayAfterSerializer : KSerializer<HolidayAfter> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(HolidayAfter::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): HolidayAfter = decoder.decodeString().let {
      if (it != "HOLIDAY_AFTER") {
        throw SerializationException(it)
      } else {
        return HolidayAfter
      }
    }
    override fun serialize(encoder: Encoder, value: HolidayAfter) = encoder.encodeString(value.value)
  }
  /** 달력일 */
  @Serializable(CalendarDaySerializer::class)
  public data object CalendarDay : PlatformSettlementCycleDatePolicy {
    override val value: String = "CALENDAR_DAY"
  }
  private object CalendarDaySerializer : KSerializer<CalendarDay> {
    override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(CalendarDay::class.java.name, PrimitiveKind.STRING)
    override fun deserialize(decoder: Decoder): CalendarDay = decoder.decodeString().let {
      if (it != "CALENDAR_DAY") {
        throw SerializationException(it)
      } else {
        return CalendarDay
      }
    }
    override fun serialize(encoder: Encoder, value: CalendarDay) = encoder.encodeString(value.value)
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformSettlementCycleDatePolicy
}


private object PlatformSettlementCycleDatePolicySerializer : KSerializer<PlatformSettlementCycleDatePolicy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformSettlementCycleDatePolicy::class.java.name, PrimitiveKind.STRING)
  override fun deserialize(decoder: Decoder): PlatformSettlementCycleDatePolicy {
    val value = decoder.decodeString()
    return when (value) {
      "HOLIDAY_BEFORE" -> PlatformSettlementCycleDatePolicy.HolidayBefore
      "HOLIDAY_AFTER" -> PlatformSettlementCycleDatePolicy.HolidayAfter
      "CALENDAR_DAY" -> PlatformSettlementCycleDatePolicy.CalendarDay
      else -> PlatformSettlementCycleDatePolicy.Unrecognized(value)
    }
  }
  override fun serialize(encoder: Encoder, value: PlatformSettlementCycleDatePolicy) = encoder.encodeString(value.value)
}
