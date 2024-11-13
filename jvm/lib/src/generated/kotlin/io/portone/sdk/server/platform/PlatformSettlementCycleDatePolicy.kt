package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 정산 기준일 */
@Serializable
public sealed class PlatformSettlementCycleDatePolicy {
  /** 공휴일 전 영업일 */
  @SerialName("HOLIDAY_BEFORE")
  public data object HolidayBefore : PlatformSettlementCycleDatePolicy()
  /** 공휴일 후 영업일 */
  @SerialName("HOLIDAY_AFTER")
  public data object HolidayAfter : PlatformSettlementCycleDatePolicy()
  /** 달력일 */
  @SerialName("CALENDAR_DAY")
  public data object CalendarDay : PlatformSettlementCycleDatePolicy()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformSettlementCycleDatePolicy()
}
