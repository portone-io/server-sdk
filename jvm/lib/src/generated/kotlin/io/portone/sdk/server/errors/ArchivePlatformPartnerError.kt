package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ArchivePlatformPartnerErrorSerializer::class)
public sealed interface ArchivePlatformPartnerError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ArchivePlatformPartnerError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ArchivePlatformPartnerError
}


private object ArchivePlatformPartnerErrorSerializer : JsonContentPolymorphicSerializer<ArchivePlatformPartnerError>(ArchivePlatformPartnerError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CANNOT_ARCHIVE_SCHEDULED_PARTNER" -> PlatformCannotArchiveScheduledPartnerError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ArchivePlatformPartnerError.Unrecognized.serializer()
  }
}
