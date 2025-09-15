package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferFilterInputCriteria
import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferStatus
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkAccountTransferFilterInput(
  val statuses: List<PlatformBulkAccountTransferStatus>? = null,
  val criteria: PlatformBulkAccountTransferFilterInputCriteria? = null,
)


