package io.portone.sdk.server.platform.payout

import kotlinx.serialization.Serializable

@Serializable
public enum class PlatformPayoutStatus {
  PREPARED,
  CANCELLED,
  STOPPED,
  PROCESSING,
  SUCCEEDED,
  FAILED,
  SCHEDULED,
}
