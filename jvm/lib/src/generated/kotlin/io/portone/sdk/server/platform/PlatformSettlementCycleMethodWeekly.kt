package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.DayOfWeek
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 매주 정해진 요일에 정산 */
@Serializable
@SerialName("WEEKLY")
public data class PlatformSettlementCycleMethodWeekly(
  /** 요일 */
  val daysOfWeek: List<DayOfWeek>,
) : PlatformSettlementCycleMethod.Recognized


