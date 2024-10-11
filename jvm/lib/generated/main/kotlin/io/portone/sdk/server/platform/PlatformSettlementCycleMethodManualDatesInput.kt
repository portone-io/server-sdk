package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.MonthDay
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformSettlementCycleMethodManualDatesInput(
  /** 월 및 일자 정보 */
  val dates: Array<MonthDay>,
)
