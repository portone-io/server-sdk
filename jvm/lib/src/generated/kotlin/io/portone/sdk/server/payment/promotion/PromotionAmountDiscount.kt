package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("AMOUNT")
public data class PromotionAmountDiscount(
  val amount: Long,
) : PromotionDiscount.Recognized


