package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 플랫폼 정산 기준일 */
@Serializable
public enum class PlatformSettlementCycleDatePolicy {
  /** 공휴일 전 영업일 */
  HOLIDAY_BEFORE,
  /** 공휴일 후 영업일 */
  HOLIDAY_AFTER,
  /** 달력일 */
  CALENDAR_DAY,
}
