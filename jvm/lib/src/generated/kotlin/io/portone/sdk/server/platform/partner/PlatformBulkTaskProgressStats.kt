package io.portone.sdk.server.platform.partner

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkTaskProgressStats(
  val preparedCount: Long,
  val processingCount: Long,
  val succeededCount: Long,
  val failedCount: Long,
  val canceledCount: Long,
)


