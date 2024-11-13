package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PlatformPayoutMethod {
  @SerialName("DIRECT")
  public data object Direct : PlatformPayoutMethod()
  @SerialName("AGENCY")
  public data object Agency : PlatformPayoutMethod()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformPayoutMethod()
}
