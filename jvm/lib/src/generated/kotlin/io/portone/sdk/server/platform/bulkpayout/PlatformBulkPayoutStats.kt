package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.platform.PlatformPayoutStatusStats
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayoutStats(
  val amount: PlatformPayoutStatusStats,
  val count: PlatformPayoutStatusStats,
)


