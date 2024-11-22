package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformBulkPayoutsErrorSerializer::class)
public sealed interface GetPlatformBulkPayoutsError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPlatformBulkPayoutsError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPlatformBulkPayoutsError
}


private object GetPlatformBulkPayoutsErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformBulkPayoutsError>(GetPlatformBulkPayoutsError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPlatformBulkPayoutsError.Unrecognized.serializer()
  }
}
