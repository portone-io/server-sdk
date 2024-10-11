package io.portone.sdk.server.platform.bulkpayout

import io.portone.sdk.server.platform.PlatformPayoutMethod
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutFilterInputCriteria
import io.portone.sdk.server.platform.bulkpayout.PlatformBulkPayoutStatus
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkPayoutFilterInput(
  val statuses: Array<PlatformBulkPayoutStatus>? = null,
  val methods: Array<PlatformPayoutMethod>? = null,
  val criteria: PlatformBulkPayoutFilterInputCriteria? = null,
)
