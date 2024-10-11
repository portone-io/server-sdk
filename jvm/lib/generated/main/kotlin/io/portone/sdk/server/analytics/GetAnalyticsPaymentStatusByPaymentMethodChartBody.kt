package io.portone.sdk.server.analytics

import io.portone.sdk.server.common.Currency
import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 고객사의 결제수단별 결제전환율 조회를 위한 입력 정보 */
@Serializable
public data class GetAnalyticsPaymentStatusByPaymentMethodChartBody(
  /** 조회할 결제 현황의 시작 시간 */
  val `from`: Instant,
  /** 조회할 결제 현황의 끝 시간 */
  val until: Instant,
  /**
   * 조회할 결제 통화
   *
   * 입력된 통화로 발생한 결제내역만 응답에 포함됩니다.
   */
  val currency: Currency,
)
