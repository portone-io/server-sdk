package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.platform.PlatformPayoutMethod
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutFilterInputCriteria
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutStatus
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayoutFilterInput(
  val statuses: List<PlatformBulkPayoutStatus>? = null,
  val methods: List<PlatformPayoutMethod>? = null,
  val criteria: PlatformBulkPayoutFilterInputCriteria? = null,
)


