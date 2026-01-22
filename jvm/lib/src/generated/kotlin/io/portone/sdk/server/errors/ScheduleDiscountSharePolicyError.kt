package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ScheduleDiscountSharePolicyErrorSerializer::class)
internal sealed interface ScheduleDiscountSharePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ScheduleDiscountSharePolicyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ScheduleDiscountSharePolicyError
}


internal object ScheduleDiscountSharePolicyErrorSerializer : JsonContentPolymorphicSerializer<ScheduleDiscountSharePolicyError>(ScheduleDiscountSharePolicyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out ScheduleDiscountSharePolicyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_ARCHIVED_DISCOUNT_SHARE_POLICY" -> PlatformArchivedDiscountSharePolicyError.serializer()
      "PLATFORM_DISCOUNT_SHARE_POLICY_NOT_FOUND" -> PlatformDiscountSharePolicyNotFoundError.serializer()
      "PLATFORM_DISCOUNT_SHARE_POLICY_SCHEDULE_ALREADY_EXISTS" -> PlatformDiscountSharePolicyScheduleAlreadyExistsError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> ScheduleDiscountSharePolicyError.Unrecognized.serializer()
    }
}
