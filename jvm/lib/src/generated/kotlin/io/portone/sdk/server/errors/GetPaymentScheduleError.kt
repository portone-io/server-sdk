package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPaymentScheduleErrorSerializer::class)
public sealed interface GetPaymentScheduleError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPaymentScheduleError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPaymentScheduleError
}


private object GetPaymentScheduleErrorSerializer : JsonContentPolymorphicSerializer<GetPaymentScheduleError>(GetPaymentScheduleError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_SCHEDULE_NOT_FOUND" -> PaymentScheduleNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPaymentScheduleError.Unrecognized.serializer()
  }
}
