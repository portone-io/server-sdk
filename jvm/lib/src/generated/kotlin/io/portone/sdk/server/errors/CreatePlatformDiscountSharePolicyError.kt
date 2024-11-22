package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformDiscountSharePolicyErrorSerializer::class)
public sealed interface CreatePlatformDiscountSharePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CreatePlatformDiscountSharePolicyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CreatePlatformDiscountSharePolicyError
}


private object CreatePlatformDiscountSharePolicyErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformDiscountSharePolicyError>(CreatePlatformDiscountSharePolicyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICY_ALREADY_EXISTS" -> PlatformDiscountSharePolicyAlreadyExistsError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformDiscountSharePolicyError.Unrecognized.serializer()
  }
}
