package io.portone.sdk.server.common

import io.portone.sdk.server.serializers.InstantSerializer
import java.time.Instant
import kotlinx.serialization.Serializable

/** 시간 범위 */
@Serializable
public data class DateTimeRange(
  val `from`: @Serializable(InstantSerializer::class) Instant,
  val until: @Serializable(InstantSerializer::class) Instant,
)
