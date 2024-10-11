package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable

/** 월 및 일자 정보 */
@Serializable
public data class MonthDay(
  val month: Int,
  val day: Int,
)
