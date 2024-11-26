package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayout
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutStatusStats
import kotlinx.serialization.Serializable

@Serializable
public data class GetPlatformBulkPayoutsResponse(
  val items: List<PlatformBulkPayout>,
  val page: PageInfo,
  val counts: PlatformBulkPayoutStatusStats,
)


