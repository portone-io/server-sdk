package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 플랫폼 정산 기준일 */
@Serializable
public sealed interface PlatformSettlementCycleDatePolicy {
  public val value: String
  /** 공휴일 전 영업일 */
  @SerialName("HOLIDAY_BEFORE")
  public data object HolidayBefore : PlatformSettlementCycleDatePolicy {
    override val value: String = "HOLIDAY_BEFORE"
  }
  /** 공휴일 후 영업일 */
  @SerialName("HOLIDAY_AFTER")
  public data object HolidayAfter : PlatformSettlementCycleDatePolicy {
    override val value: String = "HOLIDAY_AFTER"
  }
  /** 달력일 */
  @SerialName("CALENDAR_DAY")
  public data object CalendarDay : PlatformSettlementCycleDatePolicy {
    override val value: String = "CALENDAR_DAY"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformSettlementCycleDatePolicy
}
