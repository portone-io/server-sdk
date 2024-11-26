package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PromotionDiscountSerializer::class)
public sealed interface PromotionDiscount {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PromotionDiscount {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PromotionDiscount
}


private object PromotionDiscountSerializer : JsonContentPolymorphicSerializer<PromotionDiscount>(PromotionDiscount::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "AMOUNT" -> PromotionAmountDiscount.serializer()
    "PERCENT" -> PromotionPercentDiscount.serializer()
    else -> PromotionDiscount.Unrecognized.serializer()
  }
}
