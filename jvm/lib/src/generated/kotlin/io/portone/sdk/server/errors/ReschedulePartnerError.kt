package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ReschedulePartnerErrorSerializer::class)
public sealed interface ReschedulePartnerError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ReschedulePartnerError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ReschedulePartnerError
}


private object ReschedulePartnerErrorSerializer : JsonContentPolymorphicSerializer<ReschedulePartnerError>(ReschedulePartnerError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_MEMBER_COMPANY_CONNECTED_PARTNER_CANNOT_BE_SCHEDULED" -> PlatformMemberCompanyConnectedPartnerCannotBeScheduledError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ReschedulePartnerError.Unrecognized.serializer()
  }
}
