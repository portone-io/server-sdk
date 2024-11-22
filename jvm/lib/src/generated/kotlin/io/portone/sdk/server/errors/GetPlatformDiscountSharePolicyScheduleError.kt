package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformDiscountSharePolicyScheduleErrorSerializer::class)
public sealed interface GetPlatformDiscountSharePolicyScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPlatformDiscountSharePolicyScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPlatformDiscountSharePolicyScheduleError
}


private object GetPlatformDiscountSharePolicyScheduleErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformDiscountSharePolicyScheduleError>(GetPlatformDiscountSharePolicyScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND" -> PlatformDiscountSharePolicyNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPlatformDiscountSharePolicyScheduleError.Unrecognized.serializer()
  }
}
