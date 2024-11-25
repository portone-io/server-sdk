package io.portone.sdk.server.platform

import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 플랫폼 중개수수료 정보 */
@Serializable(PlatformFeeSerializer::class)
public sealed interface PlatformFee {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PlatformFee {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PlatformFee
}


private object PlatformFeeSerializer : JsonContentPolymorphicSerializer<PlatformFee>(PlatformFee::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FIXED_AMOUNT" -> PlatformFixedAmountFee.serializer()
    "FIXED_RATE" -> PlatformFixedRateFee.serializer()
    else -> PlatformFee.Unrecognized.serializer()
  }
}
