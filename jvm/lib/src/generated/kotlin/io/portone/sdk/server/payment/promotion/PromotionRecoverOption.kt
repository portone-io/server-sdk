package io.portone.sdk.server.payment.promotion

import kotlinx.serialization.KSerializer
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
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PromotionRecoverOption {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PromotionRecoverOption
}


public object PromotionRecoverOptionSerializer : JsonContentPolymorphicSerializer<PromotionRecoverOption>(PromotionRecoverOption::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PromotionRecoverOption> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "NO_RECOVER" -> PromotionRecoverOptionNoRecover.serializer()
      "RECOVER" -> PromotionRecoverOptionRecover.serializer()
      else -> PromotionRecoverOption.Unrecognized.serializer()
    }
}
