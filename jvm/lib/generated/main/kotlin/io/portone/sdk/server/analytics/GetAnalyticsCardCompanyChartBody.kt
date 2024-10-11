package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsTimeGranularity
import io.portone.sdk.server.analytics.CardCompany
import io.portone.sdk.server.common.Currency
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 고객사의 카드사별 결제 현황 조회를 위한 입력 정보 */
@Serializable
public data class GetAnalyticsCardCompanyChartBody(
  /** 조회할 카드사별 결제 현황의 시작 시간 */
  val `from`: Instant,
  /** 조회할 카드사별 결제 현황의 끝 시간 */
  val until: Instant,
  /**
   * 조회할 결제 통화
   *
   * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
   */
  val currency: Currency,
  /**
   * 결제취소건 제외 여부
   *
   * true 이면 결제취소내역은 응답에 포함 및 반영되지 않습니다. false 또는 값을 명시하지 않은 경우 결제취소내역이 응답에 반영됩니다.
   */
  val excludeCancelled: Boolean,
  /**
   * 카드사별 결제 현황 조회 단위
   *
   * 시간별, 월별 단위만 지원됩니다.
   */
  val timeGranularity: AnalyticsTimeGranularity,
  /** 조회할 카드사 */
  val cardCompanies: Array<CardCompany>,
  /** 나머지 집계에 포함되지 않을 카드사 */
  val excludesFromRemainders: Array<CardCompany>,
)