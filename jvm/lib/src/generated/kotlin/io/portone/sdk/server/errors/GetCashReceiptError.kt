package io.portone.sdk.server.errors

import kotlin.String
import kotlinx.serialization.KSerializer
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.JsonClassDiscriminator
import kotlinx.serialization.json.JsonContentPolymorphicSerializer
import kotlinx.serialization.json.JsonElement
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive

@Serializable(GetCashReceiptErrorSerializer::class)
internal sealed interface GetCashReceiptError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : GetCashReceiptError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : GetCashReceiptError
}


internal object GetCashReceiptErrorSerializer : JsonContentPolymorphicSerializer<GetCashReceiptError>(GetCashReceiptError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out GetCashReceiptError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "CASH_RECEIPT_NOT_FOUND" -> CashReceiptNotFoundError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> GetCashReceiptError.Unrecognized.serializer()
    }
}
