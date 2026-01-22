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

@Serializable(PayWithBillingKeyErrorSerializer::class)
internal sealed interface PayWithBillingKeyError {
  @Serializable
  @JsonClassDiscriminator("type")
  /** 현재 SDK 버전에서 처리 가능한 응답을 나타냅니다. */
  public sealed interface Recognized : PayWithBillingKeyError {
    public val message: String?
  }
  /** 현재 SDK 버전에서 알 수 없는 응답을 나타냅니다. */
  @Serializable
  public data object Unrecognized : PayWithBillingKeyError
}


internal object PayWithBillingKeyErrorSerializer : JsonContentPolymorphicSerializer<PayWithBillingKeyError>(PayWithBillingKeyError::class) {
  override fun selectDeserializer(element: JsonElement): KSerializer<out PayWithBillingKeyError> =
    when (element.jsonObject["type"]?.jsonPrimitive?.contentOrNull) {
      "ALREADY_PAID" -> AlreadyPaidError.serializer()
      "BILLING_KEY_ALREADY_DELETED" -> BillingKeyAlreadyDeletedError.serializer()
      "BILLING_KEY_NOT_FOUND" -> BillingKeyNotFoundError.serializer()
      "CHANNEL_NOT_FOUND" -> ChannelNotFoundError.serializer()
      "DISCOUNT_AMOUNT_EXCEEDS_TOTAL_AMOUNT" -> DiscountAmountExceedsTotalAmountError.serializer()
      "FORBIDDEN" -> ForbiddenError.serializer()
      "INVALID_REQUEST" -> InvalidRequestError.serializer()
      "MAX_TRANSACTION_COUNT_REACHED" -> MaxTransactionCountReachedError.serializer()
      "PAYMENT_SCHEDULE_ALREADY_EXISTS" -> PaymentScheduleAlreadyExistsError.serializer()
      "PG_PROVIDER" -> PgProviderError.serializer()
      "PROMOTION_PAY_METHOD_DOES_NOT_MATCH" -> PromotionPayMethodDoesNotMatchError.serializer()
      "SUM_OF_PARTS_EXCEEDS_TOTAL_AMOUNT" -> SumOfPartsExceedsTotalAmountError.serializer()
      "UNAUTHORIZED" -> UnauthorizedError.serializer()
      else -> PayWithBillingKeyError.Unrecognized.serializer()
    }
}
