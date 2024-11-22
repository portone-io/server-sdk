package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CancelPlatformPartnerScheduleErrorSerializer::class)
public sealed interface CancelPlatformPartnerScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CancelPlatformPartnerScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CancelPlatformPartnerScheduleError
}


private object CancelPlatformPartnerScheduleErrorSerializer : JsonContentPolymorphicSerializer<CancelPlatformPartnerScheduleError>(CancelPlatformPartnerScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CancelPlatformPartnerScheduleError.Unrecognized.serializer()
  }
}
