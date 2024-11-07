package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.Serializable

@Serializable
public enum class PlatformBulkPayoutStatus {
  Scheduled,
  Preparing,
  Prepared,
  Ongoing,
  Cancelled,
  Stopped,
  Completed,
}
