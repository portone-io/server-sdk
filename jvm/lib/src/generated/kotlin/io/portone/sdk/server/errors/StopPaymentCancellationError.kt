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

@Serializable(StopPaymentCancellationErrorSerializer::class)
internal sealed interface StopPaymentCancellationError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : StopPaymentCancellationError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : StopPaymentCancellationError
}


internal object StopPaymentCancellationErrorSerializer : JsonContentPolymorphicSerializer<StopPaymentCancellationError>(StopPaymentCancellationError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out StopPaymentCancellationError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "PAYMENT_CANCELLATION_NOT_FOUND" -> PaymentCancellationNotFoundError.serializer()
      "PAYMENT_CANCELLATION_NOT_PENDING" -> PaymentCancellationNotPendingError.serializer()
      "PAYMENT_NOT_FOUND" -> PaymentNotFoundError.serializer()
      "PG_PROVIDER" -> PgProviderError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> StopPaymentCancellationError.Unrecognized.serializer()
    }
}
