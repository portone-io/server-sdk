package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformAdditionalFeePoliciesErrorSerializer::class)
public sealed interface GetPlatformAdditionalFeePoliciesError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPlatformAdditionalFeePoliciesError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPlatformAdditionalFeePoliciesError
}


private object GetPlatformAdditionalFeePoliciesErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformAdditionalFeePoliciesError>(GetPlatformAdditionalFeePoliciesError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPlatformAdditionalFeePoliciesError.Unrecognized.serializer()
  }
}
