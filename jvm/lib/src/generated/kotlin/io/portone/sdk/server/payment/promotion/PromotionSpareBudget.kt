package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator

@Serializable
@JsonClassDiscriminator("type")
public sealed interface PromotionSpareBudget {
  public sealed interface Recognized : PromotionSpareBudget {
  }
  public data object Unrecognized : PromotionSpareBudget
}
