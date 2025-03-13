package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetB2bBusinessInfosErrorSerializer::class)
internal sealed interface GetB2bBusinessInfosError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : GetB2bBusinessInfosError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : GetB2bBusinessInfosError
}


private object GetB2bBusinessInfosErrorSerializer : JsonContentPolymorphicSerializer<GetB2bBusinessInfosError>(GetB2bBusinessInfosError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "B2B_EXTERNAL_SERVICE" -> B2bExternalServiceError.serializer()
    "B2B_NOT_ENABLED" -> B2bNotEnabledError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetB2bBusinessInfosError.Unrecognized.serializer()
  }
}
