package io.portone.sdk.server.platform.transfer

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

/** 간편 결제 수단 */
@Serializable
public sealed interface EasyPayMethodType {
  public val value: String
  @SerialName("CARD")
  public data object Card : EasyPayMethodType {
    override val value: String = "CARD"
  }
  @SerialName("TRANSFER")
  public data object Transfer : EasyPayMethodType {
    override val value: String = "TRANSFER"
  }
  @SerialName("CHARGE")
  public data object Charge : EasyPayMethodType {
    override val value: String = "CHARGE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : EasyPayMethodType
}
