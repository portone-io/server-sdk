package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CancelPlatformDiscountSharePolicyScheduleErrorSerializer::class)
public sealed interface CancelPlatformDiscountSharePolicyScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CancelPlatformDiscountSharePolicyScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CancelPlatformDiscountSharePolicyScheduleError
}


private object CancelPlatformDiscountSharePolicyScheduleErrorSerializer : JsonContentPolymorphicSerializer<CancelPlatformDiscountSharePolicyScheduleError>(CancelPlatformDiscountSharePolicyScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND" -> PlatformDiscountSharePolicyNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CancelPlatformDiscountSharePolicyScheduleError.Unrecognized.serializer()
  }
}
