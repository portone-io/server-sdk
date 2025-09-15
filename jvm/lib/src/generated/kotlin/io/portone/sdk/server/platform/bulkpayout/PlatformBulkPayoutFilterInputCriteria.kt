package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.common.DateTimeRange
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayoutFilterInputCriteria(
  /** 생성 일시 범위 */
  val timestampRange: DateTimeRange? = null,
  /** 상태 업데이트 일시 범위 */
  val statusUpdatedTimestampRange: DateTimeRange? = null,
  /** 일괄 지급 아이디 */
  val bulkPayoutId: String? = null,
)


