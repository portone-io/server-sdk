package io.portone.sdk.server.platform

import kotlin.IntArray
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformSettlementCycleMethodMonthlyInput(
  val daysOfMonth: IntArray,
)
