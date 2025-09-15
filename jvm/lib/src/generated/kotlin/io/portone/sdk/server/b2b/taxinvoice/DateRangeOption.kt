package io.portone.sdk.server.b2b.taxinvoice

import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class DateRangeOption(
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val `from`: String? = null,
  /**
   * 날짜를 나타내는 문자열로, `yyyy-MM-dd` 형식을 따릅니다.
   * (yyyy-MM-dd)
   */
  val until: String? = null,
)


