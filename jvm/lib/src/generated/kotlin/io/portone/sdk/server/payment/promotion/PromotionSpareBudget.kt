package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.KSerializer
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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PromotionSpareBudget {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PromotionSpareBudget
}


public object PromotionSpareBudgetSerializer : JsonContentPolymorphicSerializer<PromotionSpareBudget>(PromotionSpareBudget::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PromotionSpareBudget> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "AMOUNT" -> PromotionSpareBudgetAmount.serializer()
      "PERCENT" -> PromotionSpareBudgetPercent.serializer()
      else -> PromotionSpareBudget.Unrecognized.serializer()
    }
}
