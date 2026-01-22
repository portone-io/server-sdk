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

@Serializable(ConfirmPaymentErrorSerializer::class)
internal sealed interface ConfirmPaymentError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : ConfirmPaymentError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : ConfirmPaymentError
}


internal object ConfirmPaymentErrorSerializer : JsonContentPolymorphicSerializer<ConfirmPaymentError>(ConfirmPaymentError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out ConfirmPaymentError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "ALREADY_PAID" -> AlreadyPaidError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INFORMATION_MISMATCH" -> InformationMismatchError.serializer()
      "INVALID_PAYMENT_TOKEN" -> InvalidPaymentTokenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
      "PG_PROVIDER" -> PgProviderError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> ConfirmPaymentError.Unrecognized.serializer()
    }
}
