package io.portone.sdk.server.platform.bulkpayout

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PlatformBulkPayoutStatus {
  @SerialName("SCHEDULED")
  public data object Scheduled : PlatformBulkPayoutStatus()
  @SerialName("PREPARING")
  public data object Preparing : PlatformBulkPayoutStatus()
  @SerialName("PREPARED")
  public data object Prepared : PlatformBulkPayoutStatus()
  @SerialName("ONGOING")
  public data object Ongoing : PlatformBulkPayoutStatus()
  @SerialName("CANCELLED")
  public data object Cancelled : PlatformBulkPayoutStatus()
  @SerialName("STOPPED")
  public data object Stopped : PlatformBulkPayoutStatus()
  @SerialName("COMPLETED")
  public data object Completed : PlatformBulkPayoutStatus()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformBulkPayoutStatus()
}
