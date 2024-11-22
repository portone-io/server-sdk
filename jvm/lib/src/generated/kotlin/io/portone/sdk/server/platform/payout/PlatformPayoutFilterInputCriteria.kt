package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.DateTimeRange
import kotlin.String
import kotlinx.serialization.Serializable

/** 검색 기준 입력 정보 */
@Serializable
public data class PlatformPayoutFilterInputCriteria(
  val timestampRange: DateTimeRange? = null,
  val payoutId: String? = null,
  val bulkPayoutId: String? = null,
)


