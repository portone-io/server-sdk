package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetCashReceiptErrorSerializer::class)
public sealed interface GetCashReceiptError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : GetCashReceiptError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : GetCashReceiptError
}


private object GetCashReceiptErrorSerializer : JsonContentPolymorphicSerializer<GetCashReceiptError>(GetCashReceiptError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CASH_RECEIPT_NOT_FOUND" -> CashReceiptNotFoundError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> GetCashReceiptError.Unrecognized.serializer()
  }
}
