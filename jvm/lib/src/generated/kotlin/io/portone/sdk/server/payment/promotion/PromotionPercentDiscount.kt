package io.portone.sdk.server.payment.promotion

import io.portone.sdk.server.payment.promotion.PromotionDiscount
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PERCENT")
public data class PromotionPercentDiscount(
  val percent: Int,
): PromotionDiscount
