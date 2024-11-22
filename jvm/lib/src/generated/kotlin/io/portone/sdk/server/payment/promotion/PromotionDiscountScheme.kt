package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PromotionDiscountSchemeSerializer::class)
public sealed interface PromotionDiscountScheme {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PromotionDiscountScheme {
  }
  @Serializable
  public data object Unrecognized : PromotionDiscountScheme
}


private object PromotionDiscountSchemeSerializer : JsonContentPolymorphicSerializer<PromotionDiscountScheme>(PromotionDiscountScheme::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "AMOUNT" -> PromotionAmountDiscountScheme.serializer()
    "PERCENT" -> PromotionPercentDiscountScheme.serializer()
    else -> PromotionDiscountScheme.Unrecognized.serializer()
  }
}
