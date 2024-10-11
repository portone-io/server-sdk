package io.portone.sdk.server.analytics

import kotlinx.serialization.Serializable

/** 고객사의 환불율 정보 */
@Serializable
public data class AnalyticsCancellationRate(
  val cancellationRate: Double,
)
