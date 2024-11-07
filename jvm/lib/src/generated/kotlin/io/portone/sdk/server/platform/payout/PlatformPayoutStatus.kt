package io.portone.sdk.server.platform.payout

import kotlinx.serialization.Serializable

@Serializable
public enum class PlatformPayoutStatus {
  Prepared,
  Cancelled,
  Stopped,
  Processing,
  Succeeded,
  Failed,
  Scheduled,
}
