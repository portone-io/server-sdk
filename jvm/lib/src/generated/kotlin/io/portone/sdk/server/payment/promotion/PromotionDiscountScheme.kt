package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PromotionDiscountScheme {
  public sealed interface Recognized : PromotionDiscountScheme {
  }
  public data object Unrecognized : PromotionDiscountScheme
}
