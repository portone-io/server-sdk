package io.portone.sdk.server.platform

import kotlin.IntArray
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 매월 정해진 날(일)에 정산 */
@Serializable
@SerialName("MONTHLY")
public data class PlatformSettlementCycleMethodMonthly(
  val daysOfMonth: IntArray,
): PlatformSettlementCycleMethod,
