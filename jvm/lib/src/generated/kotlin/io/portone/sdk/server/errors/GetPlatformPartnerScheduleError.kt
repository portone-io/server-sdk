package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPlatformPartnerScheduleErrorSerializer::class)
public sealed interface GetPlatformPartnerScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPlatformPartnerScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPlatformPartnerScheduleError
}


private object GetPlatformPartnerScheduleErrorSerializer : JsonContentPolymorphicSerializer<GetPlatformPartnerScheduleError>(GetPlatformPartnerScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPlatformPartnerScheduleError.Unrecognized.serializer()
  }
}
