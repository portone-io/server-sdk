package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.common.PageInput
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutFilterInput
import kotlinx.serialization.Serializable

@Serializable
public data class GetPlatformBulkPayoutsBody(
  val isForTest: Boolean? = null,
  val page: PageInput? = null,
  val filter: PlatformBulkPayoutFilterInput? = null,
)
