package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(SchedulePartnerErrorSerializer::class)
public sealed interface SchedulePartnerError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : SchedulePartnerError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : SchedulePartnerError
}


private object SchedulePartnerErrorSerializer : JsonContentPolymorphicSerializer<SchedulePartnerError>(SchedulePartnerError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED" -> PlatformAccountVerificationAlreadyUsedError.serializer()
    "PLATFORM_ACCOUNT_VERIFICATION_FAILED" -> PlatformAccountVerificationFailedError.serializer()
    "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND" -> PlatformAccountVerificationNotFoundError.serializer()
    "PLATFORM_ARCHIVED_PARTNER" -> PlatformArchivedPartnerError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_INSUFFICIENT_DATA_TO_CHANGE_PARTNER_TYPE" -> PlatformInsufficientDataToChangePartnerTypeError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "PLATFORM_PARTNER_SCHEDULE_ALREADY_EXISTS" -> PlatformPartnerScheduleAlreadyExistsError.serializer()
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> SchedulePartnerError.Unrecognized.serializer()
  }
}
