package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable
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
  public data object HolidayBefore : PlatformSettlementCycleDatePolicy {
    override val value: String = "HOLIDAY_BEFORE"
  }
  /** 공휴일 후 영업일 */
  public data object HolidayAfter : PlatformSettlementCycleDatePolicy {
    override val value: String = "HOLIDAY_AFTER"
  }
  /** 달력일 */
  public data object CalendarDay : PlatformSettlementCycleDatePolicy {
    override val value: String = "CALENDAR_DAY"
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformSettlementCycleDatePolicy
}


private object PlatformSettlementCycleDatePolicySerializer : KSerializer<PlatformSettlementCycleDatePolicy> {
  override val descriptor: SerialDescriptor = PrimitiveSerialDescriptor(PlatformSettlementCycleDatePolicy::class.java.canonicalName, PrimitiveKind.STRING)
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
