package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePlatformContractErrorSerializer::class)
public sealed interface CreatePlatformContractError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CreatePlatformContractError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CreatePlatformContractError
}


private object CreatePlatformContractErrorSerializer : JsonContentPolymorphicSerializer<CreatePlatformContractError>(CreatePlatformContractError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CONTRACT_ALREADY_EXISTS" -> PlatformContractAlreadyExistsError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePlatformContractError.Unrecognized.serializer()
  }
}
