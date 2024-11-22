package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ResendWebhookErrorSerializer::class)
public sealed interface ResendWebhookError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ResendWebhookError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ResendWebhookError
}


private object ResendWebhookErrorSerializer : JsonContentPolymorphicSerializer<ResendWebhookError>(ResendWebhookError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "MAX_WEBHOOK_RETRY_COUNT_REACHED" -> MaxWebhookRetryCountReachedError.serializer()
    "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    "WEBHOOK_NOT_FOUND" -> WebhookNotFoundError.serializer()
    else -> ResendWebhookError.Unrecognized.serializer()
  }
}
