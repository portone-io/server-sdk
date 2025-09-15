package io.portone.sdk.server.platform.bulkaccounttransfer

import io.portone.sdk.server.platform.PlatformAccountTransferStatusStats
import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkAccountTransferStats(
  val amount: PlatformAccountTransferStatusStats,
  val count: PlatformAccountTransferStatusStats,
)


