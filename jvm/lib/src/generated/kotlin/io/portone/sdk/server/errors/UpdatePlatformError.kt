package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(UpdatePlatformErrorSerializer::class)
public sealed interface UpdatePlatformError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : UpdatePlatformError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : UpdatePlatformError
}


private object UpdatePlatformErrorSerializer : JsonContentPolymorphicSerializer<UpdatePlatformError>(UpdatePlatformError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PLATFORM_INVALID_SETTLEMENT_FORMULA" -> PlatformInvalidSettlementFormulaError.serializer()
    "PLATFORM_NOT_ENABLED" -> PlatformNotEnabledError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> UpdatePlatformError.Unrecognized.serializer()
  }
}
