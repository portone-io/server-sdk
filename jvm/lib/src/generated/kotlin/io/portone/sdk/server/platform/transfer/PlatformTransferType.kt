package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PlatformTransferType {
  @SerialName("ORDER")
  public data object Order : PlatformTransferType()
  @SerialName("ORDER_CANCEL")
  public data object OrderCancel : PlatformTransferType()
  @SerialName("MANUAL")
  public data object Manual : PlatformTransferType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PlatformTransferType()
}
