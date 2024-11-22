package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CancelPlatformContractScheduleErrorSerializer::class)
public sealed interface CancelPlatformContractScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CancelPlatformContractScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CancelPlatformContractScheduleError
}


private object CancelPlatformContractScheduleErrorSerializer : JsonContentPolymorphicSerializer<CancelPlatformContractScheduleError>(CancelPlatformContractScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_CONTRACT_NOT_FOUND" -> PlatformContractNotFoundError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CancelPlatformContractScheduleError.Unrecognized.serializer()
  }
}
