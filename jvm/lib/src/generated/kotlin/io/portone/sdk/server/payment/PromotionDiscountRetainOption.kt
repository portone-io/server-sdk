package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed interface PromotionDiscountRetainOption {
  public val value: String
  @SerialName("RETAIN")
  public data object Retain : PromotionDiscountRetainOption {
    override val value: String = "RETAIN"
  }
  @SerialName("RELEASE")
  public data object Release : PromotionDiscountRetainOption {
    override val value: String = "RELEASE"
  }
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(override val value: String) : PromotionDiscountRetainOption
}
