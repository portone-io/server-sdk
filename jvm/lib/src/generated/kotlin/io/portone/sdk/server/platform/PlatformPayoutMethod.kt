package io.portone.sdk.server.platform

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PlatformPayoutMethod {
  public val value: String
  @SerialName("DIRECT")
  public data object Direct : PlatformPayoutMethod {
    override val value: String = "DIRECT"
  }
  @SerialName("AGENCY")
  public data object Agency : PlatformPayoutMethod {
    override val value: String = "AGENCY"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformPayoutMethod
}
