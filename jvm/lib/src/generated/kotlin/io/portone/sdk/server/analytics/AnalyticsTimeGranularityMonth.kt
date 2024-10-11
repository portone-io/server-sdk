package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 월 */
@Serializable
public data class AnalyticsTimeGranularityMonth(
  val timezoneHourOffset: Int,
)
