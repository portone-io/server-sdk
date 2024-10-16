package io.portone.sdk.server.platform.payout

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.payout.PlatformPayoutFilterInput
import kotlinx.serialization.Serializable

@Serializable
internal data class GetPlatformPayoutsBody(
  val isForTest: Boolean? = null,
  val page: PageInput? = null,
  val filter: PlatformPayoutFilterInput? = null,
)
