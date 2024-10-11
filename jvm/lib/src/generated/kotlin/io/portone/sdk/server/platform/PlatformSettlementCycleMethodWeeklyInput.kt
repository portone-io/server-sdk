package io.portone.sdk.server.platform

import io.portone.sdk.server.common.DayOfWeek
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformSettlementCycleMethodWeeklyInput(
  /** 요일 */
  val daysOfWeek: List<DayOfWeek>,
)
