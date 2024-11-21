package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface CancelRequester {
  public val value: String
  @SerialName("CUSTOMER")
  public data object Customer : CancelRequester {
    override val value: String = "CUSTOMER"
  }
  @SerialName("ADMIN")
  public data object Admin : CancelRequester {
    override val value: String = "ADMIN"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : CancelRequester
}
