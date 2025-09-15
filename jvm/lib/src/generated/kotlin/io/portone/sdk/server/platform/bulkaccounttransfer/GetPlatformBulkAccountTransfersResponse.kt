package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.common.PageInfo
import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransfer
import io.portone.sdk.server.platform.bulkaccounttransfer.PlatformBulkAccountTransferStatusStats
import kotlinx.serialization.Serializable

@Serializable
public data class GetPlatformBulkAccountTransfersResponse(
  val items: List<PlatformBulkAccountTransfer>,
  val page: PageInfo,
  val counts: PlatformBulkAccountTransferStatusStats,
)


