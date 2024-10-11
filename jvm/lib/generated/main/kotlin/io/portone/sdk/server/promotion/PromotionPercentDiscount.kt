package io.portone.sdk.server.promotion

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
@SerialName("PERCENT")
public data class PromotionPercentDiscount(
  val percent: Int,
): PromotionDiscount,
