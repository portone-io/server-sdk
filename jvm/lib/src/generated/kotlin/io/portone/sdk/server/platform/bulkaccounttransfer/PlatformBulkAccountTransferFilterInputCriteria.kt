package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.common.DateTimeRange
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkAccountTransferFilterInputCriteria(
  /** 생성 일시 범위 */
  val timestampRange: DateTimeRange? = null,
  /** 상태 업데이트 일시 범위 */
  val statusUpdatedTimestampRange: DateTimeRange? = null,
  /** 일괄 이체 아이디 */
  val bulkAccountTransferId: String? = null,
)


