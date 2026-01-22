package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CancelPlatformPartnerScheduleErrorSerializer::class)
internal sealed interface CancelPlatformPartnerScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : CancelPlatformPartnerScheduleError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : CancelPlatformPartnerScheduleError
}


internal object CancelPlatformPartnerScheduleErrorSerializer : JsonContentPolymorphicSerializer<CancelPlatformPartnerScheduleError>(CancelPlatformPartnerScheduleError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out CancelPlatformPartnerScheduleError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
      "PLATFORM_PARTNER_NOT_FOUND" -> PlatformPartnerNotFoundError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> CancelPlatformPartnerScheduleError.Unrecognized.serializer()
    }
}
