package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformManualTransferErrorSerializer::class)
public sealed interface CreatePlatformManualTransferError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CreatePlatformManualTransferError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CreatePlatformManualTransferError
}


private object CreatePlatformManualTransferErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformManualTransferError>(CreatePlatformManualTransferError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "PLATFORM_USER_DEFINED_PROPERTY_NOT_FOUND" -> PlatformUserDefinedPropertyNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformManualTransferError.Unrecognized.serializer()
  }
}
