package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformPartnerErrorSerializer::class)
public sealed interface CreatePlatformPartnerError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CreatePlatformPartnerError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CreatePlatformPartnerError
}


private object CreatePlatformPartnerErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformPartnerError>(CreatePlatformPartnerError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ACCOUNT_VERIFICATION_ALREADY_USED" -> PlatformAccountVerificationAlreadyUsedError.serializer()
    "PLATFORM_ACCOUNT_VERIFICATION_FAILED" -> PlatformAccountVerificationFailedError.serializer()
    "PLATFORM_ACCOUNT_VERIFICATION_NOT_FOUND" -> PlatformAccountVerificationNotFoundError.serializer()
    "PLATFORM_COMPANY_VERIFICATION_ALREADY_USED" -> PlatformCompanyVerificationAlreadyUsedError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_CURRENCY_NOT_SUPPORTED" -> PlatformCurrencyNotSupportedError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_ID_ALREADY_EXISTS" -> PlatformPartnerIdAlreadyExistsError.serializer()
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformPartnerError.Unrecognized.serializer()
  }
}
