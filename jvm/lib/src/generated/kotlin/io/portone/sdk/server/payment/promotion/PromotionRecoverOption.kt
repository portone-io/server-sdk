package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(PromotionRecoverOptionSerializer::class)
public sealed interface PromotionRecoverOption {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : PromotionRecoverOption {
  }
  @Serializable
  public data object Unrecognized : PromotionRecoverOption
}


private object PromotionRecoverOptionSerializer : JsonContentPolymorphicSerializer<PromotionRecoverOption>(PromotionRecoverOption::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "NO_RECOVER" -> PromotionRecoverOptionNoRecover.serializer()
    "RECOVER" -> PromotionRecoverOptionRecover.serializer()
    else -> PromotionRecoverOption.Unrecognized.serializer()
  }
}
