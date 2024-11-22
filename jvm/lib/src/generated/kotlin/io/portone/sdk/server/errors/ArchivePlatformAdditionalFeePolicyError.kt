package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ArchivePlatformAdditionalFeePolicyErrorSerializer::class)
public sealed interface ArchivePlatformAdditionalFeePolicyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ArchivePlatformAdditionalFeePolicyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ArchivePlatformAdditionalFeePolicyError
}


private object ArchivePlatformAdditionalFeePolicyErrorSerializer : JsonContentPolymorphicSerializer<ArchivePlatformAdditionalFeePolicyError>(ArchivePlatformAdditionalFeePolicyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_ADDITIONAL_FEE_POLICY_NOT_FOUND" -> PlatformAdditionalFeePolicyNotFoundError.serializer()
    "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_ADDITIONAL_FEE_POLICY" -> PlatformCannotArchiveScheduledAdditionalFeePolicyError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ArchivePlatformAdditionalFeePolicyError.Unrecognized.serializer()
  }
}
