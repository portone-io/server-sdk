package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformPartnerFilterOptionsErrorSerializer::class)
internal sealed interface GetPlatformPartnerFilterOptionsError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : GetPlatformPartnerFilterOptionsError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : GetPlatformPartnerFilterOptionsError
}


internal object GetPlatformPartnerFilterOptionsErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformPartnerFilterOptionsError>(GetPlatformPartnerFilterOptionsError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out GetPlatformPartnerFilterOptionsError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> GetPlatformPartnerFilterOptionsError.Unrecognized.serializer()
    }
}
