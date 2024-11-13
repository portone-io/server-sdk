package io.portone.sdk.server.payment

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
public sealed class PromotionDiscountRetainOption {
  @SerialName("RETAIN")
  public data object Retain : PromotionDiscountRetainOption()
  @SerialName("RELEASE")
  public data object Release : PromotionDiscountRetainOption()
  @ConsistentCopyVisibility
  public data class Unrecognized internal constructor(public val value: String) : PromotionDiscountRetainOption()
}
