package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ScheduleAdditionalFeePolicyErrorSerializer::class)
public sealed interface ScheduleAdditionalFeePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ScheduleAdditionalFeePolicyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ScheduleAdditionalFeePolicyError
}


private object ScheduleAdditionalFeePolicyErrorSerializer : JsonContentPolymorphicSerializer<ScheduleAdditionalFeePolicyError>(ScheduleAdditionalFeePolicyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND" -> PlatformAdditionalFeePolicyNotFoundError.serializer()
    "PLATFORM_ADDITIONAL_FEE_POLICY_SCHEDULE_ALREADY_EXISTS" -> PlatformAdditionalFeePolicyScheduleAlreadyExistsError.serializer()
    "PLATFORM_ARCHIVED_ADDITIONAL_FEE_POLICY" -> PlatformArchivedAdditionalFeePolicyError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ScheduleAdditionalFeePolicyError.Unrecognized.serializer()
  }
}
