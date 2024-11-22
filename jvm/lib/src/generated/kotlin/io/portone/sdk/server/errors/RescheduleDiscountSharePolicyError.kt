package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(RescheduleDiscountSharePolicyErrorSerializer::class)
public sealed interface RescheduleDiscountSharePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : RescheduleDiscountSharePolicyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : RescheduleDiscountSharePolicyError
}


private object RescheduleDiscountSharePolicyErrorSerializer : JsonContentPolymorphicSerializer<RescheduleDiscountSharePolicyError>(RescheduleDiscountSharePolicyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND" -> PlatformDiscountSharePolicyNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> RescheduleDiscountSharePolicyError.Unrecognized.serializer()
  }
}
