package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 주 */
@Serializable
public data class AnalyticsTimeGranularityWeek(
  val timezoneHourOffset: Int,
)
