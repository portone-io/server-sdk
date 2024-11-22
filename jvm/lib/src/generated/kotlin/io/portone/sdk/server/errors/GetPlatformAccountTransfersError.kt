package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformAccountTransfersErrorSerializer::class)
public sealed interface GetPlatformAccountTransfersError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPlatformAccountTransfersError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPlatformAccountTransfersError
}


private object GetPlatformAccountTransfersErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformAccountTransfersError>(GetPlatformAccountTransfersError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPlatformAccountTransfersError.Unrecognized.serializer()
  }
}
