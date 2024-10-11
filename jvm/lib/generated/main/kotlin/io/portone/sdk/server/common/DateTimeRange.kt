package io.portone.sdk.server.common

import kotlinx.datetime.Instant
import kotlinx.serialization.Serializable

/** 시간 범위 */
@Serializable
public data class DateTimeRange(
  val `from`: Instant,
  val until: Instant,
)
