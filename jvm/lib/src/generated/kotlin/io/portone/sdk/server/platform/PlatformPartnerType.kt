package io.portone.sdk.server.platform

import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

/** 파트너 유형별 추가 정보 */
@Serializable(PlatformPartnerTypeSerializer::class)
public sealed interface PlatformPartnerType {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PlatformPartnerType {
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PlatformPartnerType
}


public object PlatformPartnerTypeSerializer : JsonContentPolymorphicSerializer<PlatformPartnerType>(PlatformPartnerType::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PlatformPartnerType> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "BUSINESS" -> PlatformPartnerTypeBusiness.serializer()
      "NON_WHT_PAYER" -> PlatformPartnerTypeNonWhtPayer.serializer()
      "WHT_PAYER" -> PlatformPartnerTypeWhtPayer.serializer()
      else -> PlatformPartnerType.Unrecognized.serializer()
    }
}
