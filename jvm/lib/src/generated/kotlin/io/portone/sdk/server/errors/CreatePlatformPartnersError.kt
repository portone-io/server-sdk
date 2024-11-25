package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformPartnersErrorSerializer::class)
public sealed interface CreatePlatformPartnersError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CreatePlatformPartnersError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CreatePlatformPartnersError
}


private object CreatePlatformPartnersErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformPartnersError>(CreatePlatformPartnersError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CONTRACTS_NOT_FOUND" -> PlatformContractsNotFoundError.serializer()
    "PLATFORM_CURRENCY_NOT_SUPPORTED" -> PlatformCurrencyNotSupportedError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_IDS_ALREADY_EXISTS" -> PlatformPartnerIdsAlreadyExistError.serializer()
    "PLATFORM_PARTNER_IDS_DUPLICATED" -> PlatformPartnerIdsDuplicatedError.serializer()
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformPartnersError.Unrecognized.serializer()
  }
}
