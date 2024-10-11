package io.portone.sdk.server.analytics

import io.portone.sdk.server.analytics.AnalyticsPaymentMethodTrendChartStat
import kotlinx.serialization.Serializable

/** 고객사의 결제수단 트렌드 차트 정보 */
@Serializable
public data class AnalyticsPaymentMethodTrendChart(
  /**
   * 결제수단별 결제금액, 결제 건수 데이터
   *
   * (timestamp, paymentMethod) 를 기준으로 오름차순 정렬되어 주어집니다.
   */
  val stats: List<AnalyticsPaymentMethodTrendChartStat>,
)
