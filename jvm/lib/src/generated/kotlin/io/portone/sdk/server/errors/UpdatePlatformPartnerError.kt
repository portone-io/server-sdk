package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(UpdatePlatformPartnerErrorSerializer::class)
public sealed interface UpdatePlatformPartnerError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : UpdatePlatformPartnerError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : UpdatePlatformPartnerError
}


private object UpdatePlatformPartnerErrorSerializer : JsonContentPolymorphicSerializer<UpdatePlatformPartnerError>(UpdatePlatformPartnerError::class) {
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
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> UpdatePlatformPartnerError.Unrecognized.serializer()
  }
}
