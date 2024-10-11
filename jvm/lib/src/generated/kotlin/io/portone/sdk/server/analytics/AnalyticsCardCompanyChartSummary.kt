package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 결제금액, 결제 건수의 총합을 나타냅니다. */
@Serializable
public data class AnalyticsCardCompanyChartSummary(
  /** 결제금액 합 */
  val totalAmount: Long,
  /** 결제 건수 합 */
  val totalCount: Long,
)
