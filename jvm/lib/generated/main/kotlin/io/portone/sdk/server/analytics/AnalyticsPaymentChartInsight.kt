package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.DayOfWeek
import kotlinx.serialization.Serializable

/** 고객사의 결제 현황 인사이트 정보 */
@Serializable
public data class AnalyticsPaymentChartInsight(
  /** 일간 최고 거래액 발생 시간 */
  val highestHourInDay: Long,
  /** 일간 최저 거래액 발생 시간 */
  val lowestHourInDay: Long,
  /** 월간 최고 거래액 발생일 */
  val highestDateInMonth: Long? = null,
  /** 월간 최저 거래액 발생일 */
  val lowestDateInMonth: Long? = null,
  /** 주간 최고 거래액 발생 요일 */
  val highestDayInWeek: DayOfWeek? = null,
  /** 주간 최저 거래액 발생 요일 */
  val lowestDayInWeek: DayOfWeek? = null,
)
