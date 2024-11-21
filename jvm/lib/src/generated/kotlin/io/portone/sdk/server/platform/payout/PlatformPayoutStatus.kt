package io.portone.sdk.server.platform.payout

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PlatformPayoutStatus {
  public val value: String
  @SerialName("PREPARED")
  public data object Prepared : PlatformPayoutStatus {
    override val value: String = "PREPARED"
  }
  @SerialName("CANCELLED")
  public data object Cancelled : PlatformPayoutStatus {
    override val value: String = "CANCELLED"
  }
  @SerialName("STOPPED")
  public data object Stopped : PlatformPayoutStatus {
    override val value: String = "STOPPED"
  }
  @SerialName("PROCESSING")
  public data object Processing : PlatformPayoutStatus {
    override val value: String = "PROCESSING"
  }
  @SerialName("SUCCEEDED")
  public data object Succeeded : PlatformPayoutStatus {
    override val value: String = "SUCCEEDED"
  }
  @SerialName("FAILED")
  public data object Failed : PlatformPayoutStatus {
    override val value: String = "FAILED"
  }
  @SerialName("SCHEDULED")
  public data object Scheduled : PlatformPayoutStatus {
    override val value: String = "SCHEDULED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutStatus
}
