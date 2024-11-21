package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PlatformBulkPayoutStatus {
  public val value: String
  @SerialName("SCHEDULED")
  public data object Scheduled : PlatformBulkPayoutStatus {
    override val value: String = "SCHEDULED"
  }
  @SerialName("PREPARING")
  public data object Preparing : PlatformBulkPayoutStatus {
    override val value: String = "PREPARING"
  }
  @SerialName("PREPARED")
  public data object Prepared : PlatformBulkPayoutStatus {
    override val value: String = "PREPARED"
  }
  @SerialName("ONGOING")
  public data object Ongoing : PlatformBulkPayoutStatus {
    override val value: String = "ONGOING"
  }
  @SerialName("CANCELLED")
  public data object Cancelled : PlatformBulkPayoutStatus {
    override val value: String = "CANCELLED"
  }
  @SerialName("STOPPED")
  public data object Stopped : PlatformBulkPayoutStatus {
    override val value: String = "STOPPED"
  }
  @SerialName("COMPLETED")
  public data object Completed : PlatformBulkPayoutStatus {
    override val value: String = "COMPLETED"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformBulkPayoutStatus
}
