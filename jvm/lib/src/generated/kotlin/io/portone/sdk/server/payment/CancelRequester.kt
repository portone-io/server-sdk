package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class CancelRequester {
  @SerialName("CUSTOMER")
  public data object Customer : CancelRequester()
  @SerialName("ADMIN")
  public data object Admin : CancelRequester()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : CancelRequester()
}
