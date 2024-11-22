package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(ConfirmEscrowErrorSerializer::class)
public sealed interface ConfirmEscrowError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : ConfirmEscrowError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : ConfirmEscrowError
}


private object ConfirmEscrowErrorSerializer : JsonContentPolymorphicSerializer<ConfirmEscrowError>(ConfirmEscrowError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
    "PAYMENT_NOT_PAID" -> PaymentNotPaidError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> ConfirmEscrowError.Unrecognized.serializer()
  }
}
