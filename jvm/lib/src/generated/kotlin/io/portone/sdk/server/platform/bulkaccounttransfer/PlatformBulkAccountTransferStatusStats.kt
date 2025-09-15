package io.portone.sdk.server.platform.bulkaccounttransfer

import kotlinx.serialization.Serializable

@Serializable
public data class PlatformBulkAccountTransferStatusStats(
  val prepared: Long,
  val scheduled: Long,
  val ongoing: Long,
  val completed: Long,
)


