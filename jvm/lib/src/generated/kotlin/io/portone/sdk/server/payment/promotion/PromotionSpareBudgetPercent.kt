package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PERCENT")
public data class PromotionSpareBudgetPercent(
  val percent: Int,
) : PromotionSpareBudget.Recognized
