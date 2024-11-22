package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(IssueBillingKeyErrorSerializer::class)
public sealed interface IssueBillingKeyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : IssueBillingKeyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : IssueBillingKeyError
}


private object IssueBillingKeyErrorSerializer : JsonContentPolymorphicSerializer<IssueBillingKeyError>(IssueBillingKeyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CHANNEL_NOT_FOUND" -> ChannelNotFoundError.serializer()
    "CHANNEL_SPECIFIC" -> ChannelSpecificError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> IssueBillingKeyError.Unrecognized.serializer()
  }
}
