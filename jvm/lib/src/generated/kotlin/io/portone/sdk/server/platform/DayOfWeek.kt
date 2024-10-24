package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 요일 */
@Serializable
public enum class DayOfWeek {
  SUN,
  MON,
  TUE,
  WED,
  THU,
  FRI,
  SAT,
}
