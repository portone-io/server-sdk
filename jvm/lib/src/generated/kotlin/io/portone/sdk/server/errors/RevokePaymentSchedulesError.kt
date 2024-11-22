package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(RevokePaymentSchedulesErrorSerializer::class)
public sealed interface RevokePaymentSchedulesError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : RevokePaymentSchedulesError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : RevokePaymentSchedulesError
}


private object RevokePaymentSchedulesErrorSerializer : JsonContentPolymorphicSerializer<RevokePaymentSchedulesError>(RevokePaymentSchedulesError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "BILLING_KEY_ALREADY_DELETED" -> BillingKeyAlreadyDeletedError.serializer()
    "BILLING_KEY_NOT_FOUND" -> BillingKeyNotFoundError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_SCHEDULE_ALREADY_PROCESSED" -> PaymentScheduleAlreadyProcessedError.serializer()
    "PAYMENT_SCHEDULE_ALREADY_REVOKED" -> PaymentScheduleAlreadyRevokedError.serializer()
    "PAYMENT_SCHEDULE_NOT_FOUND" -> PaymentScheduleNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> RevokePaymentSchedulesError.Unrecognized.serializer()
  }
}
