package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetPaymentErrorSerializer::class)
public sealed interface GetPaymentError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetPaymentError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetPaymentError
}


private object GetPaymentErrorSerializer : JsonContentPolymorphicSerializer<GetPaymentError>(GetPaymentError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetPaymentError.Unrecognized.serializer()
  }
}
