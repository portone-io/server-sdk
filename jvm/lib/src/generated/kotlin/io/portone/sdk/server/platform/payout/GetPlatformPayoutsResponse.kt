package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.PlatformPayoutStatusStats
import io.portone.sdk.server.platform.payout.PlatformPayout
import kotlinx.serialization.Serializable

@Serializable
public data class GetPlatformPayoutsResponse(
  val items: List<PlatformPayout>,
  val page: PageInfo,
  val counts: PlatformPayoutStatusStats,
)
