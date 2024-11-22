package io.portone.sdk.server.platform

import io.portone.sdk.server.platform.MonthDay
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 정해진 날짜(월, 일)에 정산 */
@Serializable
@SerialName("MANUAL_DATES")
public data class PlatformSettlementCycleMethodManualDates(
  /** 월 및 일자 정보 */
  val dates: List<MonthDay>,
) : PlatformSettlementCycleMethod.Recognized


