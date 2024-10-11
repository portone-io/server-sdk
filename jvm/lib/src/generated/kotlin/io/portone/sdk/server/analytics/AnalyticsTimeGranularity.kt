package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsTimeGranularityDay
import io.portone.sdk.server.analytics.AnalyticsTimeGranularityHour
import io.portone.sdk.server.analytics.AnalyticsTimeGranularityMinute
import io.portone.sdk.server.analytics.AnalyticsTimeGranularityMonth
import io.portone.sdk.server.analytics.AnalyticsTimeGranularityWeek
import kotlinx.serialization.Serializable

/**
 * 조회 시간 단위
 *
 * 하나의 단위 필드만 선택하여 입력합니다.
 */
@Serializable
public data class AnalyticsTimeGranularity(
  val minute: AnalyticsTimeGranularityMinute? = null,
  val hour: AnalyticsTimeGranularityHour? = null,
  val day: AnalyticsTimeGranularityDay? = null,
  val week: AnalyticsTimeGranularityWeek? = null,
  val month: AnalyticsTimeGranularityMonth? = null,
)
