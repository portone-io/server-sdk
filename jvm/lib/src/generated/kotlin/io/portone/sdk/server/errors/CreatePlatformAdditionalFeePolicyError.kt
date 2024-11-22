package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformAdditionalFeePolicyErrorSerializer::class)
public sealed interface CreatePlatformAdditionalFeePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CreatePlatformAdditionalFeePolicyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CreatePlatformAdditionalFeePolicyError
}


private object CreatePlatformAdditionalFeePolicyErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformAdditionalFeePolicyError>(CreatePlatformAdditionalFeePolicyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ADDITIONAL_FEE_POLICY_ALREADY_EXISTS" -> PlatformAdditionalFeePolicyAlreadyExistsError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformAdditionalFeePolicyError.Unrecognized.serializer()
  }
}
