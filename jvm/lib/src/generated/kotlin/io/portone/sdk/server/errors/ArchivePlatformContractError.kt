package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ArchivePlatformContractErrorSerializer::class)
public sealed interface ArchivePlatformContractError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ArchivePlatformContractError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ArchivePlatformContractError
}


private object ArchivePlatformContractErrorSerializer : JsonContentPolymorphicSerializer<ArchivePlatformContractError>(ArchivePlatformContractError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_CONTRACT" -> PlatformCannotArchiveScheduledContractError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ArchivePlatformContractError.Unrecognized.serializer()
  }
}
