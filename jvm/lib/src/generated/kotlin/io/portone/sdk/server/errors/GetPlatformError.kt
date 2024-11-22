package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformErrorSerializer::class)
public sealed interface GetPlatformError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPlatformError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPlatformError
}


private object GetPlatformErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformError>(GetPlatformError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPlatformError.Unrecognized.serializer()
  }
}
