package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.common.DateTimeRange
import kotlin.String
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayoutFilterInputCriteria(
  val timestampRange: DateTimeRange? = null,
  val bulkPayoutId: String? = null,
)
