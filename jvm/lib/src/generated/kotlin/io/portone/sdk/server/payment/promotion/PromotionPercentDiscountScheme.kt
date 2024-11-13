package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PERCENT")
public data class PromotionPercentDiscountScheme(
  val percent: Int,
) : PromotionDiscountScheme
