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

@Serializable(ConnectPartnerMemberCompanyErrorSerializer::class)
internal sealed interface ConnectPartnerMemberCompanyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ConnectPartnerMemberCompanyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ConnectPartnerMemberCompanyError
}


internal object ConnectPartnerMemberCompanyErrorSerializer : JsonContentPolymorphicSerializer<ConnectPartnerMemberCompanyError>(ConnectPartnerMemberCompanyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out ConnectPartnerMemberCompanyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_BTX_NOT_ENABLED" -> PlatformBtxNotEnabledError.serializer()
      "PLATFORM_EXTERNAL_API_FAILED" -> PlatformExternalApiFailedError.serializer()
      "PLATFORM_MEMBER_COMPANY_NOT_CONNECTABLE_STATUS" -> PlatformMemberCompanyNotConnectableStatusError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
      "PLATFORM_PARTNER_SCHEDULE_EXISTS" -> PlatformPartnerScheduleExistsError.serializer()
      "PLATFORM_PARTNER_TAXATION_TYPE_IS_SIMPLE" -> PlatformPartnerTaxationTypeIsSimpleError.serializer()
      "PLATFORM_PARTNER_TYPE_IS_NOT_BUSINESS" -> PlatformPartnerTypeIsNotBusinessError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> ConnectPartnerMemberCompanyError.Unrecognized.serializer()
    }
}
