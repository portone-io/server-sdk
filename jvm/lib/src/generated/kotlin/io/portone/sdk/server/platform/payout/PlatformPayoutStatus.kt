package io.portone.sdk.server.platform.payout

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PlatformPayoutStatus {
  @SerialName("PREPARED")
  public data object Prepared : PlatformPayoutStatus()
  @SerialName("CANCELLED")
  public data object Cancelled : PlatformPayoutStatus()
  @SerialName("STOPPED")
  public data object Stopped : PlatformPayoutStatus()
  @SerialName("PROCESSING")
  public data object Processing : PlatformPayoutStatus()
  @SerialName("SUCCEEDED")
  public data object Succeeded : PlatformPayoutStatus()
  @SerialName("FAILED")
  public data object Failed : PlatformPayoutStatus()
  @SerialName("SCHEDULED")
  public data object Scheduled : PlatformPayoutStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPayoutStatus()
}
