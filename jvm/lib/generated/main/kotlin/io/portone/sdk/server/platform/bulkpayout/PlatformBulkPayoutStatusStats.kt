package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayoutStatusStats(
  val preparing: Long,
  val prepared: Long,
  val ongoing: Long,
  val stopped: Long,
  val cancelled: Long,
  val completed: Long,
)
