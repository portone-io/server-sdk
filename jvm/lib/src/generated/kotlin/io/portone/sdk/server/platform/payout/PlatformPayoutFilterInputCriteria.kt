package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.DateTimeRange
import kotlin.String
import kotlinx.serialization.Serializable

/** 검색 기준 입력 정보 */
@Serializable
public data class PlatformPayoutFilterInputCriteria(
  /** 시간 범위 */
  val timestampRange: DateTimeRange? = null,
  /** 지급 아이디 */
  val payoutId: String? = null,
  /** 일괄 지급 아이디 */
  val bulkPayoutId: String? = null,
)


