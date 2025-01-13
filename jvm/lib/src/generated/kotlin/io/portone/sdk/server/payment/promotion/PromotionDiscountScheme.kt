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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PromotionDiscountScheme {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
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
