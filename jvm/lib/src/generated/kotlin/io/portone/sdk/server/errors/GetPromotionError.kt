package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPromotionErrorSerializer::class)
public sealed interface GetPromotionError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPromotionError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPromotionError
}


private object GetPromotionErrorSerializer : JsonContentPolymorphicSerializer<GetPromotionError>(GetPromotionError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PROMOTION_NOT_FOUND" -> PromotionNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPromotionError.Unrecognized.serializer()
  }
}
