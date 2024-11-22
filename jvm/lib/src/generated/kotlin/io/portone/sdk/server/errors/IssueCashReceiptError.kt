package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(IssueCashReceiptErrorSerializer::class)
public sealed interface IssueCashReceiptError {
  @Serializable
  @JsonClassDiscriminator("type")
  public sealed interface Recognized : IssueCashReceiptError {
    public val message: String?
  }
  @Serializable
  public data object Unrecognized : IssueCashReceiptError
}


private object IssueCashReceiptErrorSerializer : JsonContentPolymorphicSerializer<IssueCashReceiptError>(IssueCashReceiptError::class) {
  override fun selectDeserializer(element: JsonElement) = when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
    "CASH_RECEIPT_ALREADY_ISSUED" -> CashReceiptAlreadyIssuedError.serializer()
    "CHANNEL_NOT_FOUND" -> ChannelNotFoundError.serializer()
    "FORBIDDEN" -> ForbiddenError.serializer()
    "INVALID_REQUEST" -> InvalidRequestError.serializer()
    "PG_PROVIDER" -> PgProviderError.serializer()
    "UNAUTHORIZED" -> UnauthorizedError.serializer()
    else -> IssueCashReceiptError.Unrecognized.serializer()
  }
}
