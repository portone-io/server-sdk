package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 일 */
@Serializable
public data class AnalyticsTimeGranularityDay(
  val timezoneHourOffset: Int,
)
