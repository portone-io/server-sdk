package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PromotionSpareBudgetSerializer::class)
public sealed interface PromotionSpareBudget {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PromotionSpareBudget {
  }
  @Serializable
  public data object Unrecognized : PromotionSpareBudget
}


private object PromotionSpareBudgetSerializer : JsonContentPolymorphicSerializer<PromotionSpareBudget>(PromotionSpareBudget::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "AMOUNT" -> PromotionSpareBudgetAmount.serializer()
    "PERCENT" -> PromotionSpareBudgetPercent.serializer()
    else -> PromotionSpareBudget.Unrecognized.serializer()
  }
}
