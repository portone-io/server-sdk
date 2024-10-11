package io.portone.sdk.server.promotion

import io.portone.sdk.server.promotion.PromotionDiscount
import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("AMOUNT")
public data class PromotionAmountDiscount(
  val amount: Long,
): PromotionDiscount
