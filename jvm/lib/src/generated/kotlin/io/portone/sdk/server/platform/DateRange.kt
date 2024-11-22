package io.portone.sdk.server.platform

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class DateRange(
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  val `from`: String,
  /** 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다. */
  val until: String,
)


