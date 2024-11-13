package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제 수단 */
@Serializable
public sealed class EasyPayMethodType {
  @SerialName("CARD")
  public data object Card : EasyPayMethodType()
  @SerialName("TRANSFER")
  public data object Transfer : EasyPayMethodType()
  @SerialName("CHARGE")
  public data object Charge : EasyPayMethodType()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : EasyPayMethodType()
}
