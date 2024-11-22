package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(CreatePaymentScheduleErrorSerializer::class)
public sealed interface CreatePaymentScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : CreatePaymentScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : CreatePaymentScheduleError
}


private object CreatePaymentScheduleErrorSerializer : JsonContentPolymorphicSerializer<CreatePaymentScheduleError>(CreatePaymentScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "ALREADY_PAID_OR_WAITING" -> AlreadyPaidOrWaitingError.serializer()
    "BILLING_KEY_ALREADY_DELETED" -> BillingKeyAlreadyDeletedError.serializer()
    "BILLING_KEY_NOT_FOUND" -> BillingKeyNotFoundError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_SCHEDULE_ALREADY_EXISTS" -> PaymentScheduleAlreadyExistsError.serializer()
    "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT" -> SumOfPartsExceedsTotalAmountError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> CreatePaymentScheduleError.Unrecognized.serializer()
  }
}
