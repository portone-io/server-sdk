package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 고객사의 해외 결제 사용 여부 */
@Serializable
public data class AnalyticsOverseasPaymentUsage(
  val isUsing: Boolean,
)
