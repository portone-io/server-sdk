package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(DeleteBillingKeyErrorSerializer::class)
public sealed interface DeleteBillingKeyError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : DeleteBillingKeyError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : DeleteBillingKeyError
}


private object DeleteBillingKeyErrorSerializer : JsonContentPolymorphicSerializer<DeleteBillingKeyError>(DeleteBillingKeyError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "BILLING_KEY_ALREADY_DELETED" -> BillingKeyAlreadyDeletedError.serializer()
    "BILLING_KEY_NOT_FOUND" -> BillingKeyNotFoundError.serializer()
    "BILLING_KEY_NOT_ISSUED" -> BillingKeyNotIssuedError.serializer()
    "CHANNEL_SPECIFIC" -> ChannelSpecificError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_SCHEDULE_ALREADY_EXISTS" -> PaymentScheduleAlreadyExistsError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> DeleteBillingKeyError.Unrecognized.serializer()
  }
}
