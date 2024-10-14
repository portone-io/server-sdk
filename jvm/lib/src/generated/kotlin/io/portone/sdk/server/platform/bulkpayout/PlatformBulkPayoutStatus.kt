package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.Serializable

@Serializable
public enum class PlatformBulkPayoutStatus {
  SCHEDULED,
  PREPARING,
  PREPARED,
  ONGOING,
  CANCELLED,
  STOPPED,
  COMPLETED,
}
