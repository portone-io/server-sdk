package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(UpdatePlatformContractErrorSerializer::class)
public sealed interface UpdatePlatformContractError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : UpdatePlatformContractError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : UpdatePlatformContractError
}


private object UpdatePlatformContractErrorSerializer : JsonContentPolymorphicSerializer<UpdatePlatformContractError>(UpdatePlatformContractError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ARCHIVED_CONTRACT" -> PlatformArchivedContractError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> UpdatePlatformContractError.Unrecognized.serializer()
  }
}
