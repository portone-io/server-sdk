package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PlatformTransferType {
  public val value: String
  @SerialName("ORDER")
  public data object Order : PlatformTransferType {
    override val value: String = "ORDER"
  }
  @SerialName("ORDER_CANCEL")
  public data object OrderCancel : PlatformTransferType {
    override val value: String = "ORDER_CANCEL"
  }
  @SerialName("MANUAL")
  public data object Manual : PlatformTransferType {
    override val value: String = "MANUAL"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PlatformTransferType
}
